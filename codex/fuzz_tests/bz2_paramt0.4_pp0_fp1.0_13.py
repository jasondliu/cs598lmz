from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

import sys

import numpy as np

from . import _pickle as pickle

from . import _dill as dill

from . import _compat

from . import _util

__all__ = ['load', 'loads', 'dump', 'dumps']

def _load(file, filename, mmap_mode=None):
    """Load numpy array from .npy, .npz or pickled format.

    Parameters
    ----------
    file : file-like object or string
        The file to read.  If file is a string, a .npy, .npz or pickled
        file is assumed; if it is a file-like object, the initialization
        will be determined by the filename and file object.
    filename : string, optional
        The filename to use for loading pickled data.
    mmap_mode : {None, 'r+', 'r', 'w+', 'c'}, optional
        If not None, then memory-map the file, using the given mode
        (see `numpy.mem
