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

for i in range(10):
    gc.collect()

latefin = None
gc.collect()
</code>
I can run it in a loop and get the desired effect only about 1/1000 times.
Edit: The above code runs much faster in PyPy (or rather, the finalization in <code>Cyclic.__del__</code> runs much faster), but it still takes a few minutes. During that time, <code>func</code> is <code>None</code>, but <code>latefin</code> is not <code>None</code>.

