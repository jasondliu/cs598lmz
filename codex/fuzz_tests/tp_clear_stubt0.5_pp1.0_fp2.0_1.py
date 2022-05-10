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

class LateFin2:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic2(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin2
        del latefin2

latefin2 = LateFin2()
func = lambda: None
cyc = tuple.__new__(Cyclic2, (func, latefin2))

func.__module__ = cyc
del func, cyc
gc.collect()

class LateFin3:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic3(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin3
        del latefin3
