import ctypes
ctypes.cast(0, ctypes.py_object)
# c_void_p

# ctypes.sizeof(ctypes.c_void_p)
# 8

# ctypes.sizeof(ctypes.py_object)
# 8

# ctypes.sizeof(ctypes.py_object) == ctypes.sizeof(ctypes.c_void_p)
# True

# ctypes.cast(0, ctypes.c_void_p)
# c_void_p(0)

# ctypes.cast(0, ctypes.py_object)
# <PyCapsule object at 0x0000026C9B9C8B10>

# ctypes.cast(0, ctypes.py_object).value
# 0

# ctypes.cast(0, ctypes.py_object).value == ctypes.cast(0, ctypes.c_void_p)
# True

# ctypes.cast(0, ctypes.py_object).value == ctypes.cast(0, ctypes.c_void_p).value

