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

# Force the cyclic object to be deleted
gc.collect()

print func
</code>
Output:
<code>&lt;weakref at 0x7fefa60f9b88; to 'function' at 0x7fefa60f9830&gt;
</code>

