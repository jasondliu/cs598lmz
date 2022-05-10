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
    func()
except TypeError:
    pass
else:
    raise AssertionError("func() should not be callable")

func = None
gc.collect()

try:
    func()
except ReferenceError:
    pass
else:
    raise AssertionError("func() should not be callable")
