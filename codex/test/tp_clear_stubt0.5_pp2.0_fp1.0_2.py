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

# This triggers the bug:
# - the finalizer of 'cyc' has been called, and the weakref to 'func'
#   has been created
# - the finalizer of 'latefin' has been called, and the weakref to
#   'func' has been set in the 'ref' attribute
# - the 'func' object is now unreachable, and it is destroyed
# - the 'func' object is destroyed, and calls its finalizer
# - the 'func' object is deallocated
# - the 'ref' attribute of 'latefin' is dereferenced
# - the weakref object is destroyed, and calls its finalizer
# - the weakref object is deallocated
# - the 'func' object is dereferenced
# - the 'func' object is deallocated again
# - the 'func' object is dereferenced again
# - the 'func' object is deallocated again
# - ...
#
# The bug is that the second deallocation of the 'func' object is
# performed without calling the finalizer, so the
