import socket
socket.if_indextoname(1)

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import numpy as np
from netCDF4 import Dataset
from matplotlib.cm import get_cmap
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from tqdm import tqdm
import pandas as pd
import glob


# In[2]:


def check1(arr,nm):
    """
    Look at the values of the variable nm in arr. If you encounter the value -1e+34, it will correct it to np.nan.
    """
    new_arr = arr[nm].copy()
