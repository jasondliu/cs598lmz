import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class X(object):
    def __init__(self):
        self.f = fun
    def __call__(self):
        return self.f()

def f():
    x = X()
    return x()

def entry_point(argv):
    res = f()
    assert res == 42
    return 0

def target(*args):
    return entry_point, None

if __name__ == '__main__':
    import sys
    entry_point(sys.argv)
