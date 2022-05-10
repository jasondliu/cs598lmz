import mmap
import numpy as np
from scipy import ndimage
import scipy.misc
import os
import sys
import random
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
from skimage import io
from skimage import exposure
from skimage import measure
from skimage import img_as_uint
from skimage import img_as_float
from skimage import img_as_ubyte
from skimage import img_as_int
from skimage.filter import threshold_otsu
from skimage.util import img_as_ubyte
from skimage.morphology import closing, square
from skimage.measure import label, regionprops
from skimage import data
from skimage.filter import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage import io
from skimage import exposure
from skimage import measure
from skimage import img_
