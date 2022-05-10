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

print(latefin.ref().__module__)
</code>
I can't think of any other way to make <code>gc</code> think that <code>func</code> is unreachable before it tries to free <code>cyc</code>.

It seems that the same thing works on CPython 3.6, but not on CPython 3.5 or CPython 2.7.

