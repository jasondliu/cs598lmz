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

# This is a regression test for a bug in the garbage collector.
# The bug was that the garbage collector would crash when it
# encountered a cyclic garbage object that had a __del__ method.
# The bug was fixed by adding a check to the garbage collector
# that skips __del__ methods if the object is part of a cycle.
#
# The test creates a cycle with two objects.  The first object
# has a __del__ method that creates a weak reference to the
# second object.  The second object has a __del__ method that
# creates a weak reference to the first object.  The weak
# references are created in such a way that the __del__ methods
# are not called until the garbage collector has already
# discovered the cycle.  The cycle is created in such a way
# that the garbage collector will visit the objects in the
# opposite order that the __del__ methods are called.
#
# The bug was that the garbage collector would crash when it
# visited the second object in the cycle.  The crash occurred
# because the garbage collector would call the __del__ method
#
