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
del func, cyc, latefin
gc.collect()

func()
</code>

It breaks the invariant of cyclic garbage collections that any object that's in the trash bin needs to be reachable from the trash bin itself. The attribute <code>__del__</code> is special: once it's called, it's deleted from the object regardless of what the <code>__del__</code> function itself does; that breaks the chain.
See also this answer by @jfs, which is where I stole the weakref trick from.

