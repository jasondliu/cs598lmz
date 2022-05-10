import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16

# the following is the important part:
# in ctypes.c_int32, ctypes.c_int16 and ctypes.c_int8
# 'short' and 'int' are different!

