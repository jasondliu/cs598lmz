import gc, weakref

import numpy as np
import dask.array as da

from . import h5
from . import util
from . import config
from . import array_split

from .util import asiterable, isiterable
from .config import config
from .array_split import array_split

from .h5 import open_h5file, close_h5file
from .h5 import get_shape, get_dtype, get_attrs


def _get_chunks(a):
    """
    Returns
    -------
    list
        A list of tuples, each tuple contains the shape of a chunk in a.
    """
    if hasattr(a, 'chunks'):
        chunks = a.chunks
    elif hasattr(a, '__array_interface__'):
        chunks = a.__array_interface__['strides']
        if chunks is None:
            chunks = a.shape
        else:
            chunks = tuple(np.abs(np.array(chunks) // a.itemsize))
    else:
        chunks = a.shape
