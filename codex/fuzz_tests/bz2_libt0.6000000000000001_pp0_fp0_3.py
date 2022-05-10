import bz2
bz2.BZ2File('./data/image-chips.tar.bz2', 'r')

import tarfile
tar = tarfile.open('./data/image-chips.tar.bz2', 'r:bz2')
tar.extractall('./data/')
tar.close()

import cv2 as cv
import numpy as np

def read_image(filename):
    img = cv.imread(filename)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    h, w, _ = img.shape
    return img, h, w

def read_images(filenames):
    images = []
    for filename in filenames:
        img, h, w = read_image(filename)
        images.append((img, h, w))
    return images

def read_image_chips(path):
    images = []
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

