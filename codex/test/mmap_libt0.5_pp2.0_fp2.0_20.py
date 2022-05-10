import mmap
import struct
import sys

import numpy as np

import pycuda.driver as cuda
import pycuda.gpuarray as gpuarray
from pycuda.compiler import SourceModule

import pycuda.tools
import pycuda.driver as drv

import cv2

# Load the image
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the size of the data
sz = img.size

# Allocate device memory and copy host to device
d_img = cuda.mem_alloc(sz)
cuda.memcpy_htod(d_img, img)

# Allocate output device memory
d_out = cuda.mem_alloc(sz)

# Compute the grid size
block_dim = (32, 16, 1)
grid_dim = (sz/block_dim[0]/block_dim[1]/block_dim[2], 1)
