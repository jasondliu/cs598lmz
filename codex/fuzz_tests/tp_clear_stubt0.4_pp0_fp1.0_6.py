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

# Create a new object to trigger the __del__ of the cyclic tuple
t = tuple()

# The weakref is now dead, and the function object is now
# uncollectable.  The function object contains a reference to the
# module object, which is also uncollectable.

# The number of uncollectable objects is the number of objects in the
# cycle, plus one for the module object.
assert gc.collect() == 2
