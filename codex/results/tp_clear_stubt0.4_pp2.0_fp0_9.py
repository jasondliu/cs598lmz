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

# The next line will crash the interpreter if the bug is present.
# The bug was that the late-deleted LateFin object was not
# cleared from the weakref dictionary, so the next time a
# LateFin object was created, it would be assigned the same
# address as the old one.  This meant that the __del__ method
# of the new object would be called twice, and the second time
# it would try to access an object that had already been deleted.
latefin = LateFin()
