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
If this is not a bug, how should I write this code so that <code>LateFin.__del__</code> is called, and the <code>func</code> is kept alive?


A:

The <code>__del__</code> method is not called for every object. A good rule of thumb is that if you're calling <code>__del__</code> yourself, you're probably doing it wrong.
In this case, you're calling <code>__del__</code> by deleting the <code>LateFin</code> instance.
<code>del latefin
</code>
This is not the same thing as deleting the reference to <code>latefin</code>; deleting the instance directly calls <code>LateFin.__del__</code>, which is not what you want.
The way it's supposed to work is that <code>LateFin.__del__</code> will be called when the object is no longer referenced by anything. When the object is no longer referenced, it will be garbage collected.

