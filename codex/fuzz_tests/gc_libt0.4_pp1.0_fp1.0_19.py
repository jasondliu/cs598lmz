import gc, weakref

import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection

from skimage.feature import peak_local_max
from skimage.measure import label, regionprops
from skimage.morphology import watershed, remove_small_objects

from . import utils

class Cell(object):
    """
    A class to represent a cell.
    """
    def __init__(self, image, image_name, position, radius,
                 intensity_map=None, intensity_map_name=None,
                 intensity_map_offset=None,
                 intensity_map_scale=None,
                 intensity_map_background=None,
                 intensity_map_threshold=None,
                 intensity_map_min_distance=None,
                
