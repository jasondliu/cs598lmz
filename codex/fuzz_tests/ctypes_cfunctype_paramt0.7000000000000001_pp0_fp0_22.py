import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)

class A():
    def __init__(self):
        self.x = 0
        self.y = 0

    def foo(self, a, b):
        self.x = a
        self.y = b
        return a

def foo(a, b):
    assert a == b
    return a

def bar(a, b):
    assert a != b
    return a

def main():
    a = A()
    a.foo(1, 2)
    assert a.x == 1
    assert a.y == 2
    f = FUNTYPE(a.foo)
    assert f(1, 2) == 1
    assert a.x == 1
    assert a.y == 2
    f = FUNTYPE(foo)
    assert f(1, 1) == 1
    assert f(1, 2) == 1
    # An exception is raised on the C side, but we don't see it
    f = FUNTYPE(bar)
    assert
