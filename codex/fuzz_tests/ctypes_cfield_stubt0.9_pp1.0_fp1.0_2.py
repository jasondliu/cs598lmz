import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

import _ctypes

def callback_func(*args):
    print(args)

CMPFUNC = ctypes.CFUNCTYPE(_ctypes._PF(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p))
cmp_func = CMPFUNC(callback_func)


def f(x, y):
    pass

class C(ctypes.Structure):
    _fields_ = [('f', CMPFUNC)]

s = S()
print(s.x)
s.x = 4
print(s.x)

c = C()
print(c.f)
c.f = cmp_func
print(c.f)

# c.f.__call__(1, 2)


# python oddities

c = C()
c.__class__.f.__set__(c, f)
c.f()


#
A = ctypes.c_int.in_dll(ctypes.CDLL(ctypes.util.find_library('
