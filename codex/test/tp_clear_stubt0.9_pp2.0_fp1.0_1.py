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

latefin = LateFin()
cyc = tuple.__new__(Cyclic, (func, latefin))

collect()
del cyc
collect()
gc.garbage[:] = []

del latefin
collect()

try:
    f = gc.garbage[0]
except IndexError:
    raise TestFailed('weakref to the __module__  attribute of an old style '
                     'function does not work')
