import gc, weakref
import numpy as np
from numpy.lib.stride_tricks import as_strided
from scipy.ndimage import map_coordinates
from scipy.spatial import KDTree
