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

# The self-referential __del__ method of "cyc" calls ref(func).
# The function object itself can't be recovered because it's part
# of a garbage-collectable cycle itself.  However func.__module__
# is still alive and func.__module__.__name__ == 'Cyclic'.
# In order for ref(func) to work, ref must honor func.__module__
# and make a reference to 'Cyclic' available.
if __name__ in 
