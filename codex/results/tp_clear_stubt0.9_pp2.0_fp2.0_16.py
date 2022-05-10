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
latefin = LateFin()
gc.collect()

assert func.__module__ is None
</code>
<code>Cyclic</code> is a <code>tuple</code> subclass because the <code>tuple</code> subclassing case was handled differently than the <code>dict</code> subclassing case.  I do now have a <code>dict</code> subclassing patch and I'll try to get it in before 3.6.0.
Thanks again for testing and providing sample code.

