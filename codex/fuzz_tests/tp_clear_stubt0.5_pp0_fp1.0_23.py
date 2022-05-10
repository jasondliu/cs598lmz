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
print(latefin.ref() is None)

# ---

# This test is a bit more tricky than the above one.  Here we
# create a cycle with a function and a custom object.  The function
# has a __module__ attribute, and the custom object has a __del__
# method.  The __del__ method of the custom object creates a weakref
# to the function.  The weakref to the function is not the last
# reference to the function, so it should not trigger the collection
# of the cycle.  However, the __del__ method also has a side effect
# of deleting the function's __module__ attribute, which is the only
# reference to the module.  The __del__ method should trigger the
# collection of the module, and the collection of the module should
# trigger the collection of the cycle.

import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __sl
