"""Create the two demonstration images for the case."""
from PIL import Image, ImageDraw
SIZE = 512

def make_ok() -> Image.Image:
    image = Image.new("RGB", (SIZE, SIZE), "#dbeafe")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((64, 64, 448, 448), radius=36, fill="#60a5fa")
    draw.text((202, 238), "OK", fill="white", stroke_width=1)
    return image

def make_defect() -> Image.Image:
    image = Image.new("RGB", (SIZE, SIZE), "#e5e7eb")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((64, 64, 448, 448), radius=36, fill="#9ca3af")
    draw.ellipse((120, 120, 392, 392), fill="#ef4444")
    draw.text((162, 238), "DEFECT", fill="white", stroke_width=1)
    return image

if __name__ == "__main__":
    make_ok().save("ok.png")
    make_defect().save("defect.png")
