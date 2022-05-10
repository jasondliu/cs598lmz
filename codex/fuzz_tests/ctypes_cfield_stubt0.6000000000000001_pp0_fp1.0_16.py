import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def check(result, func, args):
    if result != func(*args):
        print func.__name__, args, '->', result, 'instead of', func(*args)

check(0, ctypes.CField.__hash__, (S.x,))
check(0, ctypes.CField.__cmp__, (S.x, S.x))
check(0, ctypes.CField.__cmp__, (S.x, 'x'))
check(-1, ctypes.CField.__cmp__, (S.x, 'y'))

try:
    ctypes.CField.__cmp__(S.x, 1)
except TypeError, e:
    pass
else:
    print 'should have raised TypeError'
