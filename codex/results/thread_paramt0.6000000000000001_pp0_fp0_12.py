import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from scipy import ndimage as ndi
from skimage import feature
from skimage import util
from skimage import filters
from skimage import morphology
from skimage import measure
from skimage import segmentation
from skimage import color
from skimage import io
from skimage import transform
from skimage import exposure
from skimage import data
from skimage.transform.hough_transform import hough_line, hough_line_peaks
from skimage.feature import canny
from skimage.morphology import watershed
from skimage.filters import sobel
from skimage.segmentation import flood, flood_fill
from skimage.feature import peak_local_max
from skimage.draw import circle_perimeter
from skimage.morphology import reconstruction
from skimage.morphology import disk
from skimage.filters import threshold_otsu
from skimage.measure import label
from sk
