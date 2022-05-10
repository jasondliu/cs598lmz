import weakref
import xarray as xr
import numpy as np
import xarray.ufuncs as xu
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from eofs.xarray import Eof

from ..core import (
    Cube,
    CubeList,
    CubeListError,
    ArrayList,
    ArrayListError,
    common,
)
from ..core.utils import (
    as_list,
    add_cyclic_point,
    add_cyclic_point_xr,
    index_of,
    broadcast_array,
)
from ..core.utils.date import dates_from_iris
from ..core.analysis.weighting import area_weights


# ----------------------------------------------------------------------
# --- Helper functions
# ----------------------------------------------------------------------
def _check_cube_data(cube, data_variable=None):
    """
    Check if the cube contains valid data.

    * If the cube has a scalar coordinate, it is removed.
    * If the cube is a singleton (i.e. has a single value for all the

