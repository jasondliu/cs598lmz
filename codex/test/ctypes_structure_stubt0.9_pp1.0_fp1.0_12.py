import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int8()
    y = ctypes.c_int8()

ctypes.pointer(S())

class S2(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int16()

ctypes.pointer(S2())
