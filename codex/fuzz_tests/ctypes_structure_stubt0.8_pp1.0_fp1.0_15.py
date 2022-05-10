import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure
    y = ctypes.Structure
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    _anonymous_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# S has two anonymous fields, x and y.
# Each of them has a field of the same name.
# So S has two anonymous fields of type c_int

################################################################

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int), ("z", ctypes.c_int)]
    _anonymous_ = [("z", ctypes.c_int)]

# S has an anonymous field 'z'.
# The original field 'z' is discarded.

################################################################

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int), ("z", ctypes.c_int)]
    _
