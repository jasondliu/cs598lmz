import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    return S()

print(f())
