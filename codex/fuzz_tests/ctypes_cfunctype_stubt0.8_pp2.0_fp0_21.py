import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ""

class X(object):
    pass

del sys.getrefcount

class Y(object):
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Z(object):
    def __reduce_ex__(self, x):
        return X, ()

class A(object):
    def __reduce_ex__(self, x):
        return Z, ()

class B(A):
    pass

class C(Z):
    pass

class D(object):
    def __reduce__(self):
        return X, ()

class E(object):
    def __reduce__(self):
        return Z, ()

class F(object):
    def __reduce__(self):
        return D, ()

class G(object):
    def __reduce_ex__(self, x):
        return D, ()

class H(object):
    pass

h = H()

