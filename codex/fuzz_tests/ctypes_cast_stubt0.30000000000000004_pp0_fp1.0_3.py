import ctypes
ctypes.cast(0, ctypes.py_object)

#%%
# The following is a simple example of a ctypes callback function.
# It prints the integer argument passed to it and returns the square of the
# argument.
#
# Note that in Python 3, the callback function cannot be directly passed as
# an argument to the foreign function. It must be wrapped in a CFUNCTYPE
# object.

from ctypes import CFUNCTYPE, c_int

# CMPFUNC = CFUNCTYPE(c_int, c_int)
# def py_cmp_func(a, b):
#     print("py_cmp_func", a, b)
#     return a - b
#
# cmp_func = CMPFUNC(py_cmp_func)
# lib.qsort.argtypes = [c_void_p, c_size_t, c_size_t, CMPFUNC]
# lib.qsort(array, len(array), c_int.size, cmp_func)

#%%
# The following example shows how to pass a Python
