import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def test_getattr():
    a = A()
    a.x = 1
    a.y = 2
    a.z = 3
    assert a.x == 1
    assert a.y == 2
    assert a.z == 3
    a.z = 4
    assert a.z == 4

def test_getattr_in_class():
    class A:
        x = 1
        y = 2
        z = 3
    a = A()
    assert a.x == 1
    assert a.y == 2
    assert a.z == 3
    a.z = 4
    assert a.z == 4

def test_getattr_inheritance():
    a = D()
    a.x = 1
    a.y = 2
    a.z = 3
    assert a.x == 1
    assert a.y == 2
    assert a.z
