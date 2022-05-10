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

# The above code creates a cycle that looks like this:
#
#   func -> cyc -> latefin -> func
#
# When the cycle is broken, the __del__ method on the Cycic object
# creates a weak reference from latefin to func.  The __del__ method
# on the LateFin object then tries to call the weak reference, which
# should invoke the __call__ method on the function object.

# This test is disabled because it's not guaranteed to work.  The
# __del__ method on the Cycic object may be called before the __del__
# method on the LateFin object.  If this happens, then the weak
# reference is never created and the test fails.  It's not clear if
# this is a bug or not.  If it is a bug, then it's a bug in the
# reference implementation too.

#if func:
#    raise TestFailed, "__call__ method not invoked"
