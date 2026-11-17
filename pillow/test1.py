from PIL import Image
import os, sys

size = (128, 128)
im = Image.open("Minecraft.png")


#Convertir les fichiers au format JPEG
# executer "python test1.py hello.jpg"
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)


#Copie d'un sous-rectangle à partir d'une image
box = (0, 0, 64, 64)
region = im.crop(box)
# region.show()#montre la sous rectangle à partir d'une image

# Traitement d'un sous-rectangle et son collage
region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)
# region.show()#montre la sous rectangle et son collage


# Défilement d'une image
def roll(im: Image.Image, delta: int) -> Image.Image:
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

new_im = roll(im, 50)
new_im.show()