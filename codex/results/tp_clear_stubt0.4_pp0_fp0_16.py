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

# This is needed because the module is not yet finalized.
# The module will be finalized later, when the func is finalized.
# But we need to force the module to be finalized now,
# because we need to make sure that the module is finalized
# before the func is finalized.
del latefin

gc.collect()

# If the module is finalized before the func, the func will be
# finalized before the module, and the func will be deleted from
# the module globals, and the module will be finalized again,
# and the func will be finalized again, and there will be a
# segfault.
#
# So, if there is no segfault, it means that the module was
# finalized before the func.
