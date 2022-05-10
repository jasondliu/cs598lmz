import ctypes

class S(ctypes.Structure):
    x = ctypes.ARRAY(ctypes.c_int, 3)
    y = ctypes.c_ushort
    z = ctypes.ARRAY(ctypes.c_byte, 2)

p = ctypes.POINTER(S)()
#
