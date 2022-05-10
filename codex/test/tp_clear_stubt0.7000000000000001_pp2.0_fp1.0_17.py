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

# If a module is cleared after being finalized, the
# __del__ method __dict__ is cleared, and the module
# dicts are cleared.  On CPython, this is not a problem,
# since modules are never finalized.  On PyPy, this is
# a problem, since modules are finalized with the
# interpreter, and the module dicts may be accessed
# during interpreter shutdown.  See issue #20290.

# This test ensures that the module dicts are cleared
# before the module is finalized, regardless of
# whether the __dict__ is cleared or not.
del latefin.__dict__

