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

# This is a regression test for the fix of issue #19375
# (https://bugs.python.org/issue19375)
# The bug was that the module object was kept alive by a reference
# from the class dict, and the cyclic garbage collector was not
# able to free the module object, which would in turn prevent the
# finalization of the class object.
#
# In the test, the module object is freed in the finalizer of the
# class object.
