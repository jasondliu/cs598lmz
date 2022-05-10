import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def g():
    raise NotImplementedError

def f():
    raise KeyboardInterrupt

def get_f():
    return f

def h(x, y, z=0, *args, **kwargs):
    pass

def i(x, y, z=0, *args, **kwargs):
    pass

def j(a, b, c=0, d=0, *e, **f):
    pass

def k(a, b, c=0, d=0, *e, **f):
    pass

def m():
    return 1

def n():
    return 1, 2

def o():
    yield 1

def p(l):
    yield from l

def q(a):
    return a

def r(a):
    return a, a

def s():
    return ()

def t():
    return [], [1, 2]

def u():
    return {}, {1: 2}

def v():
    return

