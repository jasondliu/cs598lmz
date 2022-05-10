import gc, weakref
import numpy as np
import numpy.ma as ma
import datetime
import os

from scipy.ndimage import gaussian_filter
from scipy.interpolate import griddata
from scipy.stats import linregress

from matplotlib.colors import LogNorm
from matplotlib.dates import date2num, num2date, DateFormatter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.dates import date2num, num2date
from matplotlib.gridspec import GridSpec
from mpl_toolkits.basemap import Basemap

from . import tools, map_tools
from . import get_data
from . import get_data as gd

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------
def get_depth(depth_file, dt=None, lat=None, lon=None):
    """
    Get the bathymetry of the domain.

    Args:
        depth
