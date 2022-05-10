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
if hasattr(latefin.ref(), '__module__'):
    print("Failed")
</code>
If you're using Python 2.6 or later (which is highly recommended), you can use the <code>gc.collect</code> function to force a collection now -- the cycle becomes uncollectable because it contains a function object in its namespace (as opposed to a dictionary object), which is a "live" object on its own.

