import mmap
import os
import re
import sys

import numpy as np

from .header import Header, _header_dtype
from .utils import _read_array_header, _read_header


class Czifile(object):
    """Read image and metadata from a .czi file.

    The Czifile class provides read-only access to image and metadata
    in a CZI file.

    Parameters
    ----------
    fname : str
        Name of the file to read.

    Attributes
    ----------
    shape : tuple
        Shape of the image array.
    dtype : numpy.dtype
        Datatype of the image array.
    axes : str
        Labels for the axes of the image array.
    axistags : str
        Human-readable description of the axes of the image array.
    metadata : dict
        Dictionary containing all of the CZI metadata.

    """

    def __init__(self, fname):
        self.fh = open(fname, "rb")
        self.mm = mmap.mmap(self.f
