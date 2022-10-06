from PIL import Image, ImageEnhance, ImageFilter
import os

### grab images from this folder and edit them by sharpening image and converting to black and white ###

path = './images'
pathOut = './editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #sharpen image and convert to black and white (L)
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splittext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')