import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def py_getattr(obj, name):
    if isinstance(obj, ctypes.CField):
        return obj.__get__(None, obj.__class__)
    else:
        return getattr(obj, name)

def py_setattr(obj, name, value):
    if isinstance(obj, ctypes.CField):
        return obj.__set__(None, value)
    else:
        return setattr(obj, name, value)

def main():
    s = S()
    s.x = 1
    print py_getattr(s, 'x')
    py_setattr(s, 'x', 2)
    print s.x
    print py_getattr(S.x, '_ctypes_')
    print py_getattr(S.x, '__doc__')
    py_setattr(S.x, '__doc__', 'new doc')
    print S.x.__doc__

if __name__ == '__main__':
    main()
