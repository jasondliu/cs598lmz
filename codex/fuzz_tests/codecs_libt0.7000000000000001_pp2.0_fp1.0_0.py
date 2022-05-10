import codecs
codecs.getreader('utf-8')(sys.stdin).encoding

# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:45:37 2020

@author: simslay
"""

import cv2
import numpy as np
import copy
import scipy.ndimage as ndi
from scipy.ndimage.filters import minimum_filter, maximum_filter
from skimage import filters
from skimage.filters import threshold_otsu

from skimage import io
from skimage.color import rgb2gray
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
from skimage.transform import rescale, resize
from skimage.exposure import rescale_intensity
from skimage.util import img_as_ubyte
from skimage.filters import threshold_otsu, threshold_local
from skimage.morphology import reconstruction
import matplotlib.pyplot as plt

from skimage.measure import label, regionprops
from skimage.exposure import adjust
