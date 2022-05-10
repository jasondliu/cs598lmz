import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure(
        x = ctypes.c_int,
        )
    y = ctypes.Structure(
        x = ctypes.c_int,
        )

assert S.x.x == S.y.x == ctypes.c_int
