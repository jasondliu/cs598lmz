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

# If the __del__ method of the LateFin object is called before the __del__
# method of the Cyclic object, then the reference in the LateFin object is
# cleared before the reference in the Cyclic object is set.  This causes
# the reference in the Cyclic object to be set to None.  The reference in
# the LateFin object is then set to None, which causes the LateFin object
# to be freed.  The reference in the Cyclic object is then set to the
# freed LateFin object, which causes a crash.

# If the __del__ method of the Cyclic object is called before the __del__
# method of the LateFin object, then the reference in the Cyclic object
# is set to the LateFin object before the reference in the LateFin object
# is cleared.  The reference in the Cyclic object is then set to None,
# which causes the Cyclic object to be freed.  The reference in the LateFin
# object is then set to None, which causes the LateFin object to be freed.
# The reference in the Cyclic object is then set to
