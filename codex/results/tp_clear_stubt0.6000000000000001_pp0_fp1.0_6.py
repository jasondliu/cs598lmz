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

# the above setup creates a cycle that is only broken after the call to gc.collect()
# the cycle consists of a function object, a tuple with one member being the function object,
# and a LateFin object with a weakref to the function object.

# the next step is to create a new LateFin object and a new weakref to the function object
# stored in latefin.ref.  the function object is not in the cycle anymore because
# the tuple no longer has a reference to it.

# now the function object is collected, and since it has a __del__,
# the tuple is put into the unreachable set, but the LateFin object is not.
# the LateFin object is freed, and the weakref in latefin.ref is called.  the weakref
# then accesses the now-freed tuple, which was not zeroed out by the GC.
# the GC then continues to collect the unreachable set and fails with a segfault.

class NewLateFin(tuple):
    __slots__ = ()
    def __del__(self):
       
