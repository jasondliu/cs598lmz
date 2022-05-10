import ctypes
ctypes.cast(0, ctypes.py_object)

del ctypes

# now the CPython implementation is gone, and the Cython implementation is used
# instead

