import ctypes
# Test ctypes.CFUNCTYPE inside ctypes
int16_p = ctypes.POINTER(ctypes.c_short)
int16_array_2d = ctypes.c_short * 200
int16_2d_p = int16_array_2d * 200
PFunc = ctypes.CFUNCTYPE(int16_p, int16_2d_p, int16_2d_p, int16_2d_p, ctypes.c_int, int16_2d_p)
PFunc()
