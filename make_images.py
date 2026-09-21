from PIL import Image, ImageDraw

SIZE = (400, 400)


def base():
    img = Image.new("RGB", SIZE, (170, 175, 180))
    d = ImageDraw.Draw(img)
    d.rectangle([40, 40, 360, 360], outline=(120, 125, 130), width=6)
    return img


ok = base()
ok.save("ok.png")

bad = base()
d = ImageDraw.Draw(bad)
d.ellipse([110, 110, 300, 300], fill=(200, 30, 25))
bad.save("defect.png")
print("saved ok.png defect.png")
