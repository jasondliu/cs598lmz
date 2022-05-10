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
del Cyclic.__del__
collect()
del LateFin.__del__
collect()
assert isinstance(latefin, LateFin)
assert func is None
del LateFin.__slots__
collect()
latefin.__init__
id(latefin)

# Check __slots__ with a strange list of slot names

class Slotted:
    __slots__ = ['f', 'f_', 'F', '__weakref__']

a = Slotted()
a.f = 1
a.f_ = 2
a.F = 3
