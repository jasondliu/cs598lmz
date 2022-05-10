import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def dotest(x, y):
    if '.' in x:
        if isinstance(y, object) or '.' in x[:x.find('.')]:
            return x
    elif isinstance(y, ctypes.CField):
        return '%s.%s' % (y.__class__.__name__, x)
    return x

print(dotest("Test","1"))
print(dotest("Test","1.2"))
print(dotest("x","1"))
print(dotest("x","1.2"))
