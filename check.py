#!/usr/bin/env python3
"""Classify an image as OK or DEFECT by its amount of red pixels."""

import argparse
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError

THRESHOLD = 0.10
MAX_SIDE = 256


def red_ratio(path: Path) -> float:
    """Return the fraction of pixels that are visibly red."""
    with Image.open(path) as source:
        image = source.convert("RGB")

    image.thumbnail((MAX_SIDE, MAX_SIDE))
    pixels = list(image.getdata())
    if not pixels:
        return 0.0

    red_pixels = sum(
        red >= 140 and red >= green * 1.5 and red >= blue * 1.5
        for red, green, blue in pixels
    )
    return red_pixels / len(pixels)


def classify(path: Path) -> tuple[str, float]:
    ratio = red_ratio(path)
    return ("DEFECT" if ratio >= THRESHOLD else "OK"), ratio


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect a defect by measuring the amount of red in an image."
    )
    parser.add_argument("image", type=Path, help="Path to a PNG, JPEG, or other image")
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
