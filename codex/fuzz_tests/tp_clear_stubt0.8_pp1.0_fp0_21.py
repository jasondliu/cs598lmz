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

for i in range(100):
    gc.collect()
    del latefin
    import __pypy__.weakproxy
    __pypy__.weakproxy.finalize_weakrefs()
    import __pypy__.weakref
    __pypy__.weakref.finalize_refs()

# this will now segfault because the weakref to `func` is not dead
del latefin
print('done')
