import ctypes
ctypes.cast("Hello", ctypes.py_object)

# for example, if you have a C function configured to accept a C 'double',
# you can pass a Python float directly to it.
libc.sin(0.5)
# 0.479425538604203

# Note that this is not limited to C functions. You can pass Python objects
# to C code anywhere you like, and conversely, you can return Python objects
# from C functions called from Python.

# You can also use ctypes to access the Python C API directly.
# The ctypes.pythonapi module contains Python/C API functions, which can
# be called as if they were normal Python functions.

ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p, ctypes.py_object, ctypes.c_char_p, ctypes.py_object, ctypes.c_int]

m = ctypes.pythonapi.Py_InitModule4("spam", None, "sp
