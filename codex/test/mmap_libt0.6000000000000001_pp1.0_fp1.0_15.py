import mmap
import numpy as np
import cv2
import sys
import os
import struct
import scipy.io as sio

def read_pfm(file):
    file = open(file, 'rb')

    color = None
    width = None
    height = None
    scale = None
    endian = None

    header = file.readline().rstrip()
