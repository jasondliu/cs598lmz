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

# This is a bit tricky.  The LateFin object is not yet dead, but it
# will be soon.  The weakref to the function is not yet dead, but it
# will be soon.  The function is not yet dead, but it will be soon.
# The only thing that is still alive is the module object.  So we
# need to make sure that the module object is not collected.  We do
# that by keeping a reference to it in the global namespace.

# The following line is the only one that matters.  It should not
# crash.
