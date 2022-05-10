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

# now, latefin.ref() is a weakref to func, but func is dead
# and the weakref is not cleared, because func is in a cycle
# with latefin.

# now, we create a new function, and make it look like the
# old one, except that it's alive.  This will confuse the
# weakref machinery and make it think that the old func is
# alive too.

def f():
    pass
f.__module__ = latefin.ref()

# now, we delete the new function, and collect again.  This
# will clear the weakref, because now func is really dead.

del f
gc.collect()

# now, latefin.ref() is None.  When we delete latefin, it
# will try to call func.  But func is dead, so this will
# segfault.

del latefin
