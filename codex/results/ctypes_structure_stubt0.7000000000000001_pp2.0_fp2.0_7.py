import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double

class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_double)
    ]

def foo(x):
    print x

def bar(x, y):
    print x, y

functype = ctypes.CFUNCTYPE(None, ctypes.c_int)

cb = functype(foo)
cb(5)

cb2 = functype(bar)
cb2(5, 6)

cb3 = functype(lambda x: print x + 1)
cb3(5)

f = lambda *args: print args
cb4 = functype(f)
cb4(5, 'foo', None)

cb5 = functype(lambda: print 'hello')
cb5()

s = S()
s.x = 5
s.y = 6

def baz(s):
    print s.x, s.y

