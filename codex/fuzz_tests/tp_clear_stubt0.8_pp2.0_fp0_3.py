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
print(latefin)
print(latefin.ref)
</code>
The Python memory allocator clears the object's memory after running <code>__del__</code> on it from an object that is not referenced anywhere.
If you use a profiler, you will see that the reference to <code>func</code> is never garbage collected.

