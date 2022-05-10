import mmap
import numpy as np
import os
import pandas as pd
import time
import sys

# function to read labels from the binary file
# label is a 1 byte integer at the start of each image
# the label is stored in the first byte of the image

def read_labels(filename):
    with open(filename, "rb") as f:
        data = np.frombuffer(f.read(), np.uint8, offset=8)
    return data
    
# function to read the images from the binary file
# the first 8 bytes of the file are a header, the rest are the images
# the images are stored as a 1D array of bytes, then reshaped into a 3D array of [index, y, x]
# where index is the image number, y is the row, and x is the column

def read_images(filename):
    with open(filename, "rb") as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, 28, 28)
    return data

#
