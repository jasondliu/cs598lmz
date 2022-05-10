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

# This is the interesting part.  We need to call the function that
# will be deleted.  If the function is called before it is deleted,
# then the function object is not freed.  If the function is called
# after it is deleted, then the function object is freed, and the
# weakref will return None.
func()

# The weakref should return None, but it doesn't.
print(latefin.ref())
