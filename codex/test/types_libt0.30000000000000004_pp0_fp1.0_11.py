import types
types.ModuleType.__getattr__ = lambda self, name: types.ModuleType(self.__name__ + '.' + name)

import numpy as np
import os
import sys
import time
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.io import imsave
from skimage.morphology import label
from skimage.measure import regionprops
from skimage.morphology import binary_dilation, binary_erosion
from skimage.morphology import disk
from skimage.measure import label, regionprops
from skimage.morphology import binary_dilation, binary_erosion
from skimage.morphology import disk
from skimage.morphology import remove_small_objects
from skimage.morphology import remove_small_holes
from skimage.measure import label, regionprops
from skimage.morphology import binary_dilation, binary_erosion
from skimage.morphology import disk
from skimage.morphology import remove_small_objects
