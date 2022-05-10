import gc, weakref
import numpy as np
import numba
from numba import jit, njit, stencil, vectorize, guvectorize, prange
import pandas as pd
import xarray as xr
import dask.array as da
from dask.distributed import Client, LocalCluster

import logging
logging.basicConfig(filename='preprocess.log',level=logging.DEBUG)

# TODO:
#   - 
#   - 
#   - 
#   - 

#%%
# ==========================================================
# ==========================================================
# ==========================================================
# ==========================================================
# ==========================================================

#%%
@jit(nopython=True)
def _get_neighbors(i, j, n, m, kernel_size=3, exclude=[-1,-1]):
    """
    Get neighbor indices of (i,j) in a (n,m) array.
    
    Parameters
    ----------
    i : int
        Row index of interest.
    j : int
        Column index of interest.

