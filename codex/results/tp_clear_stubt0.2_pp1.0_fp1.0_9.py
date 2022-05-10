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
# The bug was that the garbage collector would not call the
# __del__ method of the LateFin object, because it was not
# reachable from the root object.
#
# The bug was fixed by adding the __del__ method of the Cyclic
# object to the list of callbacks to be called when the Cyclic
# object is destroyed.
#
# The bug was introduced in Python 2.2a1.
#
# The bug was fixed in Python 2.2a2.

# The bug was reintroduced in Python 2.2a3.
#
# The bug was fixed in Python 2.2a4.

# The bug was reintroduced in Python 2.2a5.
#
# The bug was fixed in Python 2.2a6.

# The bug was reintroduced in Python 2.2a7.
#
# The bug was fixed in Python 2.2a8.

# The bug was reintroduced in Python 2.2a9.
#
# The bug was fixed in Python
