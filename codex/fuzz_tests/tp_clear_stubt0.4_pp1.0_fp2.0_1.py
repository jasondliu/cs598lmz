import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect()
assert latefin.ref() is None
del latefin
gc.collect()
assert func is None

# ____________________________________________________________

def f():
    pass

def g():
    pass

f.func_code = g.func_code

import sys
sys.modules['__main__'].f = f

del f, g
gc.collect()

# ____________________________________________________________

def f():
    pass

def g():
    pass

f.func_code = g.func_code

import sys
sys.modules['__main__'].f = f

del f, g
gc.collect()

# ____________________________________________________________

def f():
    pass

def g():
    pass

f.func_code = g.func_code

import sys
sys.modules['__main__'].f = f

del f, g
gc.collect()

# ____________________________________________________________

def f(a, b, c, d, e, f, g, h, i, j, k
