from PIL import Image



#All image format available can be found at https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

image_to_convert = Image.open('sample.webp')
image_to_convert.save('converted-image.png', 'png')