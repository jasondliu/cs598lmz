import mmap

import cv2
import numpy as np

import sys
sys.path.append("../../")
import config

def get_image_binary(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    return data

def get_image_binary_mmap(image_path):
    with open(image_path, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            return m

def get_image_binary_cv(image_path):
    img = cv2.imread(image_path)
    data = cv2.imencode('.jpg', img)[1].tostring()
    return data

def get_image_binary_np(image_path):
    img = cv2.imread(image_path)
    data = np.array(img)
    data = data.tostring()
    return data

def get_image_binary_np_cv
