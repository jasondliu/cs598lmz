import ctypes
# Test ctypes.CFUNCTYPE by wrapping drand48
rand_t = ctypes.CFUNCTYPE(ctypes.c_double)
lib = ctypes.CDLL(None)
drand48 = lib.drand48
