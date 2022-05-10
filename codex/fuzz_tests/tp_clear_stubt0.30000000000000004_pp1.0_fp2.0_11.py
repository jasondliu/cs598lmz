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

# This is the test.  If the bug is present, the next line will fail.
# If the bug is not present, the next line will succeed.
latefin.ref()()

# If the bug is not present, this line will succeed.
# If the bug is present, this line will fail.
del latefin

gc.collect()

# If the bug is not present, this line will succeed.
# If the bug is present, this line will fail.
del func
