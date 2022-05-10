import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __init__(self, *args):
        super(X, self).__init__(*args)
        self.name = 'xyz'

class Y(ctypes.CField):
    def __init__(self, *args):
        super(Y, self).__init__(*args)
        self.name = 'abc'

class Z(ctypes.CField):
    def __init__(self, *args):
        super(Z, self).__init__(*args)
        self.name = 'def'

class A(ctypes.Structure):
    _fields_ = [('a', X), ('b', Y), ('c', Z)]

class B(ctypes.Structure):
    _fields_ = [('b', A)]

print(A.a.name)
print(B.b._fields_[0][1].a.name)
</code>
I'm trying to create a class that inherits from <code>ctypes.CField</code>, and then I want to
