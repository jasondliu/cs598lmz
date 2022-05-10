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

# For CPython, the latefin object is never destroyed, because it's referred to
# by the module (attached to its func_globals) and by the gc.garbage list.
# See the "Cycles involving modules" section of gcmodule.c.
#
# For PyPy, the latefin object *is* destroyed, because it's not referred to by
# anything (the module still gets destroyed even that it contains a
# reference to it).
