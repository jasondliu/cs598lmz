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

class C:
    def __init__(self, x):
        self.x = x
    def __getstate__(self):
        return self.x
    def __setstate__(self, state):
        print(state)
        self.x = state

for i in range(0, 10):
    func.__module__ = C(0)
