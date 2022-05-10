import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

prototypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),
              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int),
              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int),
              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int),
              ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c
