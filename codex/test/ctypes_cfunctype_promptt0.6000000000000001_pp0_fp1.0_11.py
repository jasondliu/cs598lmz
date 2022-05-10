import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x, y: x)(1, 2)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x, y=1: x)(1, 2)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x, y=1: x)(1)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x)(1, 2)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y=1: x)(1, 2)
# Test c
