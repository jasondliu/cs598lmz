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

# crashes the interpreter

# the following is a workaround for a bug in the garbage collector
# that I found in Python 2.4.1

class WeakCyclic(tuple):
    __slots__ = ()
    def __init__(self):
        self[1].ref = weakref.ref(self[0])
cyc = tuple.__new__(WeakCyclic, (lambda: None, LateFin()))
del cyc
