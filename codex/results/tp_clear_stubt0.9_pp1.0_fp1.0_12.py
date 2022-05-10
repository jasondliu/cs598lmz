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
print gc.collect()
</code>
This raises an exception; or maybe just crashes, but 'a' doesn't get printed twice.
The second approach is to have a separate weakref to the function (or bound method) as used on sys.modules; as you can see here: keep a reference alive <code>lr = weakref.ref(self)</code>; if <code>sys.modules</code> gets cleared of the reference to the function, and the function gets destroyed, then the weakref doesn't die; and the weakref has a direct reference to the function, and the finaliser only runs when the weakref does.

