import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from cv2 import cv2
import numpy as np
from skimage import io
from time import time
from matplotlib import pyplot as plt
from skimage.util import img_as_ubyte
from skimage.transform import rescale, rotate
from skimage.feature import canny
from skimage.filters import gaussian
from skimage.draw import circle_perimeter
from skimage.morphology import reconstruction
from skimage.morphology import disk
from skimage.morphology import square, rectangle
from skimage.morphology import watershed
from skimage.measure import label
from skimage.measure import regionprops
from skimage.measure import label, regionprops
from scipy.ndimage import distance_transform_edt as distance
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import KMeans

from scipy.ndimage import binary_fill_holes
from scipy import ndimage as ndi
from scipy.ndimage.
