import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64()


def f():
    return S()

