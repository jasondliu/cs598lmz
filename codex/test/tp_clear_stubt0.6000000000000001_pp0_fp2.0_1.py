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
gc.collect()
gc.collect()

assert latefin.ref() is None

import gc, weakref

class C:
    __slots__ = ('__dict__', '__weakref__')

gc.collect()
gc.collect()
gc.collect()

c = C()
c.x = 1
c.y = 2
w = weakref.ref(c)
c.z = 3

del c
gc.collect()
gc.collect()
gc.collect()

assert w().z == 3

import gc, weakref

class C:
    __slots__ = ('__dict__', '__weakref__', 'x')

gc.collect()
gc.collect()
gc.collect()

c = C()
w = weakref.ref(c)
c.x = 1

del c
gc.collect()
gc.collect()
gc.collect()

assert w().x == 1

import gc, weakref

