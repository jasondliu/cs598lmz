import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = ctypes.c_int(0)

def f():
    C().x

def g():
    S().x

def main():
    f()
    g()
    return 0

def target(*args):
    return main, None

if __name__ == "__main__":
    import sys
    main()
