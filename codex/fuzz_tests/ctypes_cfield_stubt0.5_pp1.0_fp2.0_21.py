import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    for i in range(1, 100000):
        s = S()
        s.x = i
        x = s.x
        assert x == i

main()
