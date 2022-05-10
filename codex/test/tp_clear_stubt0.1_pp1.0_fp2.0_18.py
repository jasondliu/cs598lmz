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

# This is a bit of a hack, but it works.
# The idea is to create a cyclic reference between a function and a
# LateFin object, and then delete the function.  The LateFin object
# will be deleted, and it will set the 'func' global to the function
# object.  Then we delete the cyclic reference and collect again.
# The function object should be collected, and the LateFin object
# should be collected.  If the function object is not collected, then
# the LateFin object will not be collected, and the 'func' global
# will not be set.

