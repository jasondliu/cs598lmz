import gc, weakref
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.colorbar as colorbar
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.ticker import MaxNLocator

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table
from astropy.nddata import Cutout2D

from scipy.interpolate import interp1d
from scipy.stats import binned_statistic
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.filters import median_filter
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.filters import minimum_filter
from scipy.ndimage.filters import percentile_filter
from scipy
