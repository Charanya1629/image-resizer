# image-resizer
 simple Python tool to **resize and convert images in batch** using [Pillow](https://python-pillow.org/).  
It takes images from the `images/` folder, resizes them to the desired size, and saves the output in the `output/` folder.
## Features
- Resize all images in a folder
- Option to **preserve aspect ratio** or force resize
- Convert image formats (JPG → PNG, PNG → JPG, etc.)
- Batch processing for multiple images
- Works on Windows, macOS, and Linux
##  Project Structure
image resizer/

│── images/ # Put your input images here

│── output/ # Resized images will be saved here

│── resizer.py # Simple version (fixed size, PNG output)

│── resizer_cli.py # Advanced version (CLI options)

│── requirements.txt # Python dependencies

│── README.md # Project documentation

│── .venv/ # Virtual environment (optional, not uploaded to GitHub)

##  Installation

1. Clone or download this repository.
2. Open terminal / PowerShell inside the project folder.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows PowerShell
   .\.venv\Scripts\Activate
   # macOS/Linux
   source .venv/bin/activate
4. Install dependencies:
   
       pip install -r requirements.txt
# Usage
1. Add Images

    Copy your images (JPG, PNG, etc.) into the images/ folder.

2. Run the Script
   Option A: Simple version
   Resizes everything to 800×800 PNG:

        python resizer.py

# CLI Options (resizer_cli.py)

| Option          | Description                            | Default |
| --------------- | -------------------------------------- | ------- |
| `--in`          | Input folder path                      | images  |
| `--out`         | Output folder path                     | output  |
| `--width`       | Target width (pixels)                  | 800     |
| `--height`      | Target height (pixels)                 | 800     |
| `--keep-aspect` | Preserve aspect ratio (fit inside box) | False   |
| `--format`      | Output format (`png` or `jpeg`)        | png     |

# Notes

- Supported formats: JPG, JPEG, PNG, BMP, GIF, TIFF

- Default behavior: converts all images to PNG

- If images/ is empty, the script will tell you to add files

- Output folder is created automatically

# Tech Stack

- Python 3.x

- Pillow (PIL Fork)




