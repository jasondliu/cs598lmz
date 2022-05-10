import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE1 = ctypes.CFUNCTYPE(ctypes.c_int)
CFUNCTYPE1(lambda : 0)
# Test ctypes.PyCFuncPtr
