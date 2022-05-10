import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    a = 1
    b = 2
    x = S(a)
    y = S(b)
    print(x.x == 1)
    print(y.x == 2)
    x.x = 3
    print(x.x == 3)
    print(y.x == 2)

main()
