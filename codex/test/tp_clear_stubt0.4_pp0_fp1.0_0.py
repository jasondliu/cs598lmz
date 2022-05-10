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
del latefin
gc.collect()

# Check that the module name is correctly removed from the function
# before it is destroyed.  If the module name is not removed, the
# function will be destroyed after the module and thus the
# function's __del__ will crash.

import gc

class A:
    def __del__(self):
        pass

a = A()
a.__module__ = a
del a
gc.collect()

# Check that a module's __del__ method is called even if the module is
# not fully initialized.

import gc

class A:
    def __del__(self):
        global gotit
        gotit = True

gotit = False
A.__module__ = A()
del A
gc.collect()
assert gotit

# Check that a module's __del__ method is called even if the module is
# not fully initialized.

import gc

class A:
    def __del__(self):
        global gotit
        gotit = True

