import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@non_reentrant(ctypes.CField)
def f(s):
    print(s.x)

s = S()
s.x = 1
f(s)
f(s)
s.x = 2
f(s)

def non_reentrant_method(t, f):
    def func(*args):
        attr = getattr(args[0], f.__name__)
        if attr.last_args:
            if t(attr.last_args, args) == 0:
                raise RuntimeError("reentrant")
        attr.last_args = args
        return f(*args)
    return func

def cmp_char_p(a, b):
    return cmp(a, b)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

S2.x.last_args = None
S2.x = non_reentrant_method(cmp_char_p, S2.x)

s2
