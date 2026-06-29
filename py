from PIL import Image, ImageDraw
import random

w,h = 1920,1080

img = Image.new("RGB",(w,h),(13,27,64))
draw = ImageDraw.Draw(img)

for _ in range(300):
    x=random.randint(0,w)
    y=random.randint(0,h)
    r=random.randint(5,40)

    draw.ellipse(
        (x-r,y-r,x+r,y+r),
        fill=(244,168,35,30)
    )

img.save("hero_background.png")

print("Saved: hero_background.png")
