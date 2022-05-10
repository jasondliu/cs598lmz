import mmap

import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"]="2"

import cv2
import numpy as np
import sys

if sys.version_info[0] == 2:
    import cPickle as pkl
