import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __getattribute__(self, name):
        if name == 'value':
            raise AttributeError
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if isinstance(value, ctypes.CField):
            raise TypeError
        object.__setattr__(self, name, value)

class B(A):
    _fields_ = [('x', ctypes.c_int)]
    def __getattribute__(self, name):
        if name == 'x':
            return 1
        return A.__getattribute__(self, name)

c = ctypes.c_int(1)
s = S(1)

print(c.value)
print(s.x)
print(B().x)

S.x = c
S.value = c

a = A()
a.x = c
a.value = c
