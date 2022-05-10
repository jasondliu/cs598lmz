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
print(latefin.ref() is None)
</code>
In Python 2, the CPython implementation adds a special case when an object has a <code>func_globals</code> attribute that is a weakrefable object (<code>type(weakref.ref(object))</code> is an unbound method), and make the object not weakrefable (by decrefing the object) instead. The object is thus freed right away, and no segfault can be triggered.
In Python 3, however, the special case is removed. The object is weakrefable, but the <code>__del__</code> doesn't run through the cycle of objects so it doesn't trigger the segfault.
This segfault probably only occurs with the CPython implementation. The write-up goes into more detail about this.

