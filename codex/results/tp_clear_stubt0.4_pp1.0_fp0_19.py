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
gc.collect()
gc.collect()

print(latefin)

# XXX: We should really be printing 'None' here.
# The problem is that the cyclic reference between 'func' and 'cyc'
# is not detected.  This is because we don't have a real __del__
# method on 'func', but a __del__ on the type.
