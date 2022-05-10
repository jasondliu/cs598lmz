import ctypes
ctypes.cast(2, ctypes.py_object)
 
# _Py_NoneStruct is an alias for None
ctypes.cast(None, ctypes.py_object)

# ints are cast to long
ctypes.cast(2, ctypes.py_object)

# so are floats
