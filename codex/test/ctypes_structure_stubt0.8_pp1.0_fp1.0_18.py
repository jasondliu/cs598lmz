import ctypes

class S(ctypes.Structure):
    x = ctypes.c_size_t

assert (ctypes.sizeof(S) % ctypes.sizeof(ctypes.c_size_t) == 0)
