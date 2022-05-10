import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# fromStruct()
s = S()
# fromStruct(s) without args doesn't work since we don't have a way to get the structure type from the struct value if it isn't a pointer.
