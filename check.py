import sys
from PIL import Image

THRESHOLD = 0.10


def red_ratio(path):
    img = Image.open(path).convert("RGB")
    img.thumbnail((256, 256))
    data = img.tobytes()
    total = len(data) // 3
    red = 0
    for i in range(0, len(data), 3):
        r, g, b = data[i], data[i + 1], data[i + 2]
        if r > 110 and r > g * 1.6 and r > b * 1.6:
            red += 1
    return red / total


def main():
    if len(sys.argv) != 2:
        print("usage: python check.py <path-to-image>")
        return 2
    ratio = red_ratio(sys.argv[1])
    print("DEFECT" if ratio >= THRESHOLD else "OK")
    print("red_ratio={:.3f} threshold={:.2f}".format(ratio, THRESHOLD))
    return 0


if __name__ == "__main__":
    sys.exit(main())
