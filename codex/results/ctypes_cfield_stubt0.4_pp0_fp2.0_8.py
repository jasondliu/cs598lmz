import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

def f(x):
    return x.x

def main():
    a = C()
    print f(a)
    b = S()
    print f(b)

main()
