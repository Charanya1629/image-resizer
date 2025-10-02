# resizer_cli.py (improved)
import sys
import os

# Dependency check
try:
    from PIL import Image
except ImportError:
    print("❌ Pillow is not installed. Run:\n    python -m pip install pillow")
    sys.exit(1)

import argparse

SUPPORTED = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

def ensure_folders(in_folder, out_folder):
    created = False
    if not os.path.exists(in_folder):
        os.makedirs(in_folder, exist_ok=True)
        print(f"📁 Created input folder: '{in_folder}'. Please add images there and rerun the script.")
        created = True
    if not os.path.exists(out_folder):
        os.makedirs(out_folder, exist_ok=True)
        print(f"📁 Created output folder: '{out_folder}'.")
    return created

def process_file(path, out_folder, size, keep_aspect, fmt):
    with Image.open(path) as img:
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        if keep_aspect:
            img.thumbnail(size, Image.LANCZOS)
        else:
            img = img.resize(size, Image.LANCZOS)
        base = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(out_folder, f"{base}.{fmt.lower()}")
        img.save(out_path, fmt.upper())
        print("✅ Saved:", out_path)

def main():
    p = argparse.ArgumentParser(description="Batch image resizer")
    p.add_argument("--in", dest="in_folder", default="images")
    p.add_argument("--out", dest="out_folder", default="output")
    p.add_argument("--width", type=int, default=800)
    p.add_argument("--height", type=int, default=800)
    p.add_argument("--keep-aspect", action="store_true", help="Preserve aspect ratio (uses thumbnail)")
    p.add_argument("--format", choices=["png","jpeg"], default="png")
    args = p.parse_args()

    size = (args.width, args.height)
    created = ensure_folders(args.in_folder, args.out_folder)
    if created:
        # If we just created the input folder, exit so user can add images
        sys.exit(0)

    files = [f for f in os.listdir(args.in_folder) if f.lower().endswith(SUPPORTED)]
    if not files:
        print(f"ℹ️ No images found in '{args.in_folder}'. Add some images (jpg/png) and rerun.")
        sys.exit(0)

    for fname in files:
        try:
            process_file(os.path.join(args.in_folder, fname), args.out_folder, size, args.keep_aspect, args.format)
        except Exception as e:
            print("⚠️ Error processing", fname, ":", e)

if __name__ == "__main__":
    main()
