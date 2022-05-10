import mmap
import struct
import os
import matplotlib.pyplot as plt
import numpy as np
import math

class Sift(object):

    def __init__(self, fname):
        # Get file size
        self.fname = fname
        self.fsize = os.stat(fname).st_size
        # Read the entire file into a byte array
        with open(fname, "rb") as f:
            self.raw = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the first 512 bytes to get the dimensions
        self.dim = struct.unpack('<ii', self.raw[:8])
        # Read the number of features
        self.nfeatures = struct.unpack('<i', self.raw[8:12])[0]
        # Read the position of the first feature
        self.pos = 12
        self.current_feature = 0
