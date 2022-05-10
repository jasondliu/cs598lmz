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

# XXX: ^^^ the above ^^^ should be the same as
# func = lambda: None
# cyc = Cyclic((func, LateFin()))
# del func, cyc

gc.collect()
if not callable(latefin.ref):
    print('Cyclic garbage collection failed')

print('OK')
