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
print(func.__module__) # should be None
print(gc.collect()) # should be 0

# Verify that the __module__ has been cleaned up
import sys
for obj in gc.get_objects():
    if obj is not None and type(obj) is type(sys) and obj.__module__ is not None:
        print("Found alive module:", obj.__name__)
        print("  module.__module__ =", obj.__module__)

# This test is complete if it doesn't crash.
