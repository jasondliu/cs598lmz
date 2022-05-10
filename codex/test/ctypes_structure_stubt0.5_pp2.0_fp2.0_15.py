import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def test(s):
    print(s.x)
    print(s.y)

s = S()
test(s)
