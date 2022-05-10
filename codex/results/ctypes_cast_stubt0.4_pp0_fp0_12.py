import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

#https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

from PIL import Image

def resize_aspect_fit():
    img = Image.open("/Users/jimmy/Desktop/test.jpg")
    width, height = img.size
    if width > height:
        delta = width - height
        left = int(delta/2)
        upper = 0
        right = height + left
        lower = height
    else:
        delta = height - width
        left = 0
        upper = int(delta/2)
        right = width
        lower = width + upper

    img = img.crop((left, upper, right, lower))
    img.thumbnail((128,128), Image.ANTIALIAS)
    img.save("/Users/jimmy/Desktop/test2.jpg")

#%%

#https://stack
