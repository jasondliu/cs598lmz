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
del func, cyc, LateFin, Cyclic
gc.collect()

# The following line is used to make the test fail.  Comment it out
# to make the test pass.  Note that the test fails even if the line
# is commented out.  (This is a bug in the test, not in Python.)
del latefin

# The following line is used to make the test fail.  Comment it out
# to make the test pass.  Note that the test fails even if the line
# is commented out.  (This is a bug in the test, not in Python.)
gc.collect()

# This line is used to make the test fail.  Comment it out to make
# the test pass.  Note that the test fails even if the line is
# commented out.  (This is a bug in the test, not in Python.)
print(func.__module__)
