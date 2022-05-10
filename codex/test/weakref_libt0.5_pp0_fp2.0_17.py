import weakref

import numpy as np

from . import _core

class _Array(np.ndarray):
    def __new__(cls, input_array, dtype=None, order=None):
        obj = np.asarray(input_array, dtype=dtype, order=order).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.__array_finalize__(obj)

    def __array_wrap__(self, out_arr, context=None):
        return np.ndarray.__array_wrap__(self, out_arr, context)

def _get_dtype(dtype):
    if dtype is None:
        return np.dtype('float32')
    if isinstance(dtype, str):
        return np.dtype(dtype)
    return dtype

def _get_order(order):
    if order is None:
        return 'C'
    if isinstance(order, str):
        return order
   
