import mmap
import numpy as np
import os
import struct
import sys
import time

from math import log10
from scipy.misc import imread, imsave, imresize
from scipy.signal import convolve2d


class BP_Stereo():
    # constructor
    def __init__(self, max_disp, disp_scale):
        self.max_disp = max_disp
        self.disp_scale = disp_scale

    def load_pfm(self, file):
        file = open(file, 'rb')

        color = None
        width = None
        height = None
