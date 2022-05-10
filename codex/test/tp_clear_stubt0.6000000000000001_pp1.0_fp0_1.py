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
del func, cyc, LateFin, Cyclic
gc.collect()
latefin.ref()

# This is a memory error in debug build.
assert gc.collect() == 0

# But in release build, it will be collected.
if not is_cli:
    del latefin
    assert gc.collect() == 2
