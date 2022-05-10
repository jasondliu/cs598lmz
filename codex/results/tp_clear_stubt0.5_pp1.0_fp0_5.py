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

print(latefin.ref())

# issue4590
import weakref

class C:
    pass

class D:
    pass

def f():
    pass

c = C()
c.f = f
c.d = D()

w = weakref.ref(c)

del c
del f

print(w().d)
