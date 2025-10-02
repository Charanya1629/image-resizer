# resizer.py
import os
from PIL import Image

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"
NEW_SIZE = (800, 800)   # width, height in pixels

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

supported_exts = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

for fname in os.listdir(INPUT_FOLDER):
    if not fname.lower().endswith(supported_exts):
        continue

    in_path = os.path.join(INPUT_FOLDER, fname)
    try:
        with Image.open(in_path) as img:
            # Optional: convert to RGB to avoid issues saving as PNG/JPEG
            if img.mode not in ("RGB", "L"):
                img = img.convert("RGB")

            # Resize (forces exact NEW_SIZE, may change aspect ratio)
            resized = img.resize(NEW_SIZE, Image.LANCZOS)

            base, _ = os.path.splitext(fname)
            out_path = os.path.join(OUTPUT_FOLDER, f"{base}.png")
            resized.save(out_path, "PNG")
            print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Error processing {fname}: {e}")
