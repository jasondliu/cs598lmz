import ctypes
ctypes.cast(1, ctypes.py_object)

#%%

import numpy as np
import ctypes

def np_array_to_pointer(array):
    """
    Converts a numpy array to a ctypes pointer
    """
    return array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

def np_array_to_pointer_pointer(array):
    """
    Converts a numpy array to a ctypes pointer to a pointer
    """
    return ctypes.cast(np_array_to_pointer(array), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))

def np_array_to_pointer_pointer_pointer(array):
    """
    Converts a numpy array to a ctypes pointer to a pointer to a pointer
    """
    return ctypes.cast(np_array_to_pointer(array), ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_double))))

def np_array_to_pointer_pointer_pointer_
