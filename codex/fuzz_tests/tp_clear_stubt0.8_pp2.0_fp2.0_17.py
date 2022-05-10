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
print(latefin())
</code>
The output is <code>None</code>, which I expected because the reference cycle should have been broken.
My question is, am I right in assuming that the reference cycle was broken, and if so, how?
The <code>Cyclic</code> class has two slots <code>__slots__</code> and <code>Cyclic.__del__</code> access the first slot <code>__slots__</code>, which is essentially a reference to <code>Cyclic.__del__</code>. The reference count of <code>__del__</code> changes, but nothing breaks the cycle as far as I can see.
Side note: As per the documentation, <code>__slots__</code> is supposed to save memory in a situation like this, but this leads to a TypeError, in case anyone is curious.


A:

Yes, the cycle was broken, but the way it was broken isn't particularly useful to anyone.
What happens is that when you create a cyclic tuple, the tuple holds a reference to the first element,
