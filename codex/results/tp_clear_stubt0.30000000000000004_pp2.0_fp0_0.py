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
gc.collect()
gc.collect()

# This is a regression test for a bug in the garbage collector.
# The bug was that the garbage collector would not call the
# __del__ method of a class if an instance of that class was part of
# a reference cycle, but the instance had a __del__ method that
# created a weak reference to the instance.
#
# The bug was originally found when the Python interpreter was
# compiled with Visual C++ 6.0, but it also shows up when Python is
# compiled with gcc.
#
# Written by: Andrew Dalke <dalke@dalkescientific.com>
# Date: 15-JUL-2001

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
