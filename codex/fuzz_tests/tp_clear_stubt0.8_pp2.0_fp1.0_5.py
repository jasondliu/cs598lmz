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
del latefin
gc.collect()

# @@@ The following test does not pass on CPython.
# In fact, the bug is the same.  If we delete the
# reference to the function later, then it is not
# finalized.  But if we postpone the finalizer
# of the function until after the other objects
# are finalized and this should work.

#class Cyclic2(tuple):
#    __slots__ = ()
#    def __del__(self):
#        self[0].ref = weakref.ref(self[1])

#class LateFin2:
#    __slots__ = ('ref',)
#    def __del__(self):
#        global func2
#        func2 = self.ref()

#func2 = lambda: None
#cyc = tuple.__new__(Cyclic, (func2, LateFin2()))

#func2.__module__ = cyc
#gc.collect()
#del func2, cyc
#gc.collect()
