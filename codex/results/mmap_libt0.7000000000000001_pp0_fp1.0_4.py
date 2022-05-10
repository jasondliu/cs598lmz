import mmap

import numpy as np

import cv2

#import pyopencl as cl

#from scipy import misc

#from scipy.misc import imread

import scipy.misc

import PIL.Image

import matplotlib.pyplot as plt

%matplotlib inline

#import os

import time

import gc

import sys

#import skimage.io

import math

import scipy.fftpack as fftpack



def resize(img, scale_percent):

width = int(img.shape[1] * scale_percent / 100)

height = int(img.shape[0] * scale_percent / 100)

dim = (width, height)

# resize image

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

return resized







def get_image(image_path):

return scipy.misc.imread(image_path, mode='RGB').astype(
