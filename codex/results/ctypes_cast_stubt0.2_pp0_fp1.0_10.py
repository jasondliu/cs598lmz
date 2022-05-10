import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a workaround for
# http://bugs.python.org/issue15881#msg170215
import os
os.stat_float_times(False)

import sys

if sys.version_info[0] == 2:
    import __builtin__ as builtins
else:
    import builtins

import numpy as np

import pytest

import dask
from dask.array.core import Array, normalize_chunks
from dask.array.utils import assert_eq, same_keys
from dask.utils import raises

from dask.array.core import (Array, blockdims_from_blockshape,
        concatenate3, concatenate4, concatenate_axes,
        from_array, from_array_blocks, from_func, from_pandas,
        from_delayed, from_zarr, from_sequence, from_npy_stack,
        getem, store, top, unpack_singleton,
        normalize_chunks, normalize
