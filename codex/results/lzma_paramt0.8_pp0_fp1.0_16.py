from lzma import LZMADecompressor
LZMADecompressor().decompress(image)

#%%
import cv2
import numpy as np

def show_image(image, title=''):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_image(image, rows=96, cols=96):
    return cv2.resize(image, (rows, cols))

def center_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        y = int(y - (h / dif_factor))
        x = int(x - (w / dif_factor))
        w = int(w + (w / (dif_factor / 2)))
        h = int(h + (h / (dif_factor / 2)))
        face = image[y:y
