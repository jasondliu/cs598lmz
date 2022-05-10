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
del latefin
gc.collect()
del func

# __del__ called twice
# http://bugs.python.org/issue23380
import gc, weakref

class A:
    def __del__(self):
        global called
        called = True

a = A()
ref = weakref.ref(a)

a = ref()

a = None
gc.collect()
del ref
gc.collect()

