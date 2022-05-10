import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a type error in Python 3
# ctypes.cast(0, ctypes.py_object)

# But this is fine
ctypes.cast(0, ctypes.c_void_p)

# This is a type error in Python 3
# ctypes.cast(0, ctypes.c_void_p).value

# But this is fine
ctypes.cast(0, ctypes.py_object).value
