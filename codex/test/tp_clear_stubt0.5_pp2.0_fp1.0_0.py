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
try:
    latefin.ref()
except ReferenceError:
    pass
else:
    raise RuntimeError('uncollectable object was not finalized')

import gc

# Issue #22851: test that cyclic garbage is collected even if
# __del__ is not called.
class C:
    def __init__(self):
        self.x = self

c = C()
weakref.ref(c)
del c
gc.collect()

# Issue #25015: test that cyclic garbage is collected even if
# __del__ raises an exception.
class C:
    def __init__(self):
        self.x = self
    def __del__(self):
        raise SystemError

c = C()
weakref.ref(c)
del c
gc.collect()

# Issue #25015: test that cyclic garbage is collected even if
# __del__ raises an exception.
class C:
    def __init__(self):
        self.x = self
    def __del__(self):
        raise
