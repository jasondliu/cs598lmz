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

# This is a bit tricky: the LateFin object is kept alive by the
# reference from the function object.  When the function object is
# destroyed, it calls the __del__ method of the LateFin object, which
# creates a new reference to the function object.  The function object
# is then destroyed again, and so on.  The function object is
# destroyed only when the LateFin object is destroyed.  This happens
# when the weak reference in the LateFin object is destroyed.  But
# this weak reference is destroyed only when the Cyclic object is
# destroyed.  The Cyclic object is destroyed only when the function
# object is destroyed.  So we have a cycle.

# The cycle is broken when the function object is destroyed.  The
# reference from the LateFin object is destroyed, and the LateFin
# object is destroyed, and the reference from the function object is
# destroyed.  The function object is then destroyed, and the Cyclic
# object is destroyed, and the reference from the function object is
# destroyed, and the function object is destroyed.  The cycle is
# broken.

