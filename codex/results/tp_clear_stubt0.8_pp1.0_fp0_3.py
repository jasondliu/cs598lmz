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

print("latefin.__dict__ has %d entries" % len(latefin.__dict__))
print("latefin.__slots__ has %d entries" % len(latefin.__slots__))
print("func.__dict__ has %d entries" % len(func.__dict__))
print("func.__slots__ has %d entries" % len(func.__slots__))
print("func.__module__ is %r" % func.__module__)
