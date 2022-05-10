import lzma
lzma.LZMAFile

import sys
import os

import numpy as np

from .file_io import *
from .data_structures import *
from . import file_io
from . import data_structures


def read_header(f):
    """Reads the header of a .dat file.

    Parameters
    ----------
    f : file
        The file object to read from.

    Returns
    -------
    header : dict
        A dictionary containing the header information.
    """
    header = {}

    # Read the file version.
    header['version'] = read_int(f)

    # Read the file type.
    header['type'] = read_int(f)

    # Read the number of dimensions.
    header['ndim'] = read_int(f)

    # Read the number of particles.
    header['npart'] = read_int(f)

    # Read the box size.
    header['boxsize'] = read_float(f)

    # Read the cosmological parameters.
    header['omega_m'] = read
