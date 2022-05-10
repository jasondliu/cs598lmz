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

assert latefin.ref() is None

# Issue #15550: before r18000, the following code would cause a crash.
# (The bug was fixed by r18000, but the test is still useful to ensure
# that the fix is not regressed.)

import gc

class A:
    def __del__(self):
        gc.collect()

class B:
    def __del__(self):
        A()

a = A()
b = B()
del a, b
gc.collect()

# Issue #16152: before r18000, the following code would crash.
# (The bug was fixed by r18000, but the test is still useful to ensure
# that the fix is not regressed.)

import gc

class A:
    def __del__(self):
        gc.collect()

class B:
    def __del__(self):
        A()

a = A()
b = B()
del a, b
gc.collect()

# Issue #12092:
