import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __set__(self, instance, value):
        super(X, self).__set__(instance, value + 1)

class C(ctypes.Structure):
    _fields_ = [('x', X)]

c = C()
c.x = 3
print c.x
</code>

