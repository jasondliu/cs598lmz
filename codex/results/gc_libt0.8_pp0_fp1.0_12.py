import gc, weakref

import pycuda.driver as drv

from pycuda.compiler import SourceModule
import pycuda.gpuarray as gpuarray

import numpy as np

import pycuda.autoinit

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import matplotlib.cm as cm

from scipy.ndimage import filters

from scipy.misc import imread

from timeit import default_timer as timer


#for plotting
class GPUPlotFilter:
    def __init__(self, img_array, filter_size = 5, block = (16, 16, 1)):
        #filter_size should be odd
        self.img_array = img_array
        self.filter_size = filter_size
        half_filter = int(np.floor(filter_size/2))
        self.filter_array = np.zeros(self.img_array.shape, dtype=np.uint8)
        self.filter_array[half_filter:-half_filter, half_filter:-half
