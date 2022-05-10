import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'Kitty on your lap'

@FUNTYPE
def fun2(a, b):
    return a + b

@FUNTYPE
def fun3(a, b, c=0, d=0):
    return a + b + c + d

@FUNTYPE
def fun4(*a):
    return sum(a)

@FUNTYPE
def fun5(**a):
    s = 0
    for key, value in a.items():
        s += key + value
    return s

@FUNTYPE
def fun6(w, x, y=1, *args):
    s = w + x + y
    for a in args:
        s += a
    return s

@FUNTYPE
def fun7(w, x, y=1, *args, **kwargs):
    s = w + x + y
    for a in args:
        s += a
    for key, value in kwargs.items():
        s += key + value
    return s

def test_cfun():
    # basic
    assert fun() == '
