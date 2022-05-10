import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

def f(s : S):
    print(repr(s))

try:
    f(S(1, 2))
except TypeError:
    print("FAIL")

try:
    f(S(z=1, y=1))
except TypeError:
    print("FAIL")
