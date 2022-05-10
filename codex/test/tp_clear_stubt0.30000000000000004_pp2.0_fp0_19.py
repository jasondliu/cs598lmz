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

# The following line would cause a crash if the bug is present.
# The bug is that the __del__ method of Cyclic is called, which
# calls the __del__ method of LateFin, which tries to access
# the func attribute of LateFin, which is a weakref to the
# func attribute of Cyclic, which has already been deleted.
# The bug is that the func attribute of Cyclic is not cleared
# when the Cyclic object is deleted.

del latefin
