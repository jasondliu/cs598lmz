import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(0x4242424242424242)
    y = ctypes.c_longlong(0x4141414141414141)

