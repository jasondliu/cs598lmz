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

import gc, weakref

class Cyclic2:
    __slots__ = ('a', 'b')
    def __del__(self):
        self.a.b = self.b
        del self.b

def run():
    global x, y, z
    x = Cyclic2()
    y = Cyclic2()
    z = Cyclic2()

    w = weakref.WeakKeyDictionary()

    x.a = y
    x.b = z
    y.a = z
    y.b = x
    z.a = x
    z.b = y
    w[x] = 1
    w[y] = 2
    w[z] = 3
    w._iterate()
    del x, y, z

run()
gc.collect()
gc.collect()

import gc, weakref

class CM:
    def __init__(self):
        self.c = weakref.WeakKeyDictionary()

class A:
    pass

