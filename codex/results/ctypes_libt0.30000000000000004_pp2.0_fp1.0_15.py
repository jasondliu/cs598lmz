import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Slider, Button, RadioButtons

import cv2
import pydicom

from skimage import measure
from skimage.transform import resize
from skimage.filters import threshold_otsu

import scipy.ndimage
from scipy.ndimage.interpolation import zoom

import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

import warnings
warnings.filterwarnings('ignore')

#%%
def get_dicom_fps(path):
    """
    Obtain the frame rate for a DICOM image
    """
    dicom_
