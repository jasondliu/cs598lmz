import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8    # Atomic type
    y = ctypes.c_char * 64  # Sequence type

