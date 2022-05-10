import gc, weakref
import numpy as np
import numpy.ma as ma
import datetime
import os

from scipy.ndimage import gaussian_filter
from scipy.interpolate import griddata
from scipy.stats import linregress

