import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    pass

class Y(X):
    _fields_ = [('a', S)]

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__,
                            ', '.join(('%s=%r' % f for f in vars(self).items())))

y = Y()
y.a.x = 100
print(y)
print(y.a)
print(y.a.x)
print(S.x)
print(S.x.__class__)
print(S.x.__class__.__bases__)
print(S.x.__class__.__bases__[0].__bases__)
print(S.x.__class__.__bases__[0].__bases__[0].__bases__)
print(S.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__)
print(S
