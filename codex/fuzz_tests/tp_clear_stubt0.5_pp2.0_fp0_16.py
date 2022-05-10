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

# This is a very tricky test: the reference to the function object is
# kept alive by the module dict and by the __del__ method.  If the
# function object is cleaned up before the module, the module will be
# left with a dangling reference to it.  If the module is cleaned up
# before the function, the __del__ method will try to call it and will
# get a reference to a freed object.  The reference to the function
# object is cleared by the module's __del__ method, but only if the
# function object is still alive.  The function object's reference to
# the module is cleared by the module's __del__ method, but only if
# the module is still alive.  So the only way to get a crash is if the
# function object and the module are both freed at the same time.
# This can happen if the weak reference in the __del__ method is not
# cleared in time.  Note that this is why the __del__ method doesn't
# just call the function directly: if it did, the reference from the
# __del__ method to the function
