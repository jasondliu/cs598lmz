import gc, weakref
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib import patches
from matplotlib.colors import Colormap, ListedColormap
from matplotlib.path import Path
from matplotlib.transforms import Bbox, TransformedBbox, IdentityTransform
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerLineCollection, HandlerPathCollection

from matplotlib.collections import PathCollection, LineCollection, PatchCollection

import shdom
import shdom.utility
import shdom.config

from scipy import interpolate, ndimage

from skimage import measure
from skimage.morphology import square

import cv2

import warnings

class ProjectionGrid(object):

    def __init__(self, shape):
        self.shape = shape
        self.shape2d = self.shape[:2]

        self
