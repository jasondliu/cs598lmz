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
weakref.ref(LateFin).__module__ = LateFin.__module__ = LateFin.ref.__module__ = 'spam'
gc.collect()
print(func.__module__)
print(LateFin.__module__)
print(LateFin.ref.__module__)
print(weakref.ref.__module__)
