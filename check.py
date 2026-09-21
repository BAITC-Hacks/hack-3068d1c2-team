#!/usr/bin/env python3
"""Print OK or DEFECT for an image based on red-pixel coverage."""
import argparse
import sys
from pathlib import Path
from PIL import Image, UnidentifiedImageError

THRESHOLD = 0.10
MAX_SIDE = 256

def red_ratio(path: Path) -> float:
    with Image.open(path) as source:
        image = source.convert("RGB")
    image.thumbnail((MAX_SIDE, MAX_SIDE))
    pixels = list(image.get_flattened_data())
    red_pixels = sum(red >= 140 and red >= green * 1.5 and red >= blue * 1.5 for red, green, blue in pixels)
    return red_pixels / len(pixels) if pixels else 0.0

def classify(path: Path) -> tuple[str, float]:
    ratio = red_ratio(path)
    return ("DEFECT" if ratio >= THRESHOLD else "OK"), ratio

def main() -> int:
    parser = argparse.ArgumentParser(description="Classify an image as OK or DEFECT.")
    parser.add_argument("image", type=Path, help="Path to an image file")
    args = parser.parse_args()
    try:
        verdict, ratio = classify(args.image)
    except FileNotFoundError:
        print(f"Error: file not found: {args.image}", file=sys.stderr)
        return 2
    except UnidentifiedImageError:
        print(f"Error: unsupported image: {args.image}", file=sys.stderr)
        return 2
    print(verdict)
    print(f"red_ratio={ratio:.3f} threshold={THRESHOLD:.2f}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

