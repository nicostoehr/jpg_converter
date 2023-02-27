from PIL import Image, ImageColor
from os import getcwd, listdir

pics = listdir(getcwd())

col = input('Hintergrund Farbe wählen( R, G, B oder #hexcode oder weiß oder schwarz ):  ')
if col.startswith('#'):
    col = ImageColor.getcolor(col, "RGB")
elif "," in col:
    t = col.split(",")
    col = (int(t[0]), int(t[1]), int(t[2]))
elif col.strip() == "weiß": col = (255, 255, 255)
elif col.strip() == "schwarz": col = (0, 0, 0)
else:
    input("Input Error! Make sure your either provide a hex color code like this:\n#e9ffe8\n\nOr an RGB value like this:\n233, 255, 232")
    sys.exit()

for pic in pics:
    if pic.endswith('.png'):
        png = Image.open(pic).convert('RGBA')
        background = Image.new('RGBA', png.size, col)

        alpha_composite = Image.alpha_composite(background, png)
        c = alpha_composite.convert('RGB')
        c.save(f'converted_{pic[:-4]}.jpg', 'JPEG', quality=100)