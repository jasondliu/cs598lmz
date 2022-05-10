import ctypes
ctypes.cast(0, ctypes.py_object)

# This will raise an exception on 32-bit platforms
ctypes.cast(0, ctypes.c_void_p)

# This will raise an exception on 64-bit platforms
