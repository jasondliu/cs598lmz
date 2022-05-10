import codecs
codecs.register_error("strict", codecs.ignore_errors)

# import numpy
# numpy.seterr(all='ignore')

import numpy as np
import math
import random
import scipy.misc
import scipy.ndimage
import skimage.color
import skimage.io
import skimage.transform
import skimage.segmentation
import skimage.filters
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import cv2

from glob import glob
from time import time
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage.filters import gaussian_filter
from multiprocessing import Pool
from skimage import data, img_as_float
from skimage.measure import label, regionprops
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)
from skimage
