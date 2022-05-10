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

# This is a bug: the LateFin object should be destroyed, and func
# should be set to None.  But the LateFin object is not destroyed
# because its ref attribute is a weakref to the Cyclic object.  The
# Cyclic object is not destroyed because its first item is a function
# that has a reference to the Cyclic object.  So the LateFin object
# is not destroyed, and func is not set to None.  The following
# assertion should fail, but doesn't.
assert func is None
