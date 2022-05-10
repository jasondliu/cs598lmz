import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    s = S()
    f = S.x
    print(type(f))
    print(f)
    print(f.__get__(s))
    print(f.__set__(s, 42))
    print(f.__set__(s, 'hello'))
    print(f.__delete__(s))

test()
