import ctypes

class S(ctypes.Structure):
    x = ("abc", ctypes.c_int)  # non-homogeneous item

