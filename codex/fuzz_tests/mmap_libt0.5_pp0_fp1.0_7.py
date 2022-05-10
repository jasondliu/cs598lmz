import mmap

import numpy as np

from .. import _utils
from .._utils import _read, _read_array, _write_array


def read_vtk(filename):
    """Read a VTK file.

    This function reads a VTK file and returns the associated data.
    The data can be accessed as a dictionary or as a structured array
    (see examples below).

    Parameters
    ----------
    filename : str
        The name of the VTK file.

    Returns
    -------
    data : dict or structured ndarray
        The VTK data.

    Examples
    --------
    >>> from skimage.measure._regionprops import read_vtk
    >>> data = read_vtk('tests/data/test_image.vtk')
    >>> data['vtk_version']
    '0.1'
    >>> data['header']
    '# vtk DataFile Version 2.0'
    >>> data['format']
    'BINARY'
    >>> data['dataset_type']
    'STRUCTURED_POINTS'
    >>> data
