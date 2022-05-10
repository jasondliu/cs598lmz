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
del func, cyc, LateFin
gc.collect()

class C:
    __slots__ = ('__weakref__', '__dict__')

c = C()
c.__dict__ = c

def func():
    return c

c.__dict__[C] = func
del c, func, C
gc.collect()
