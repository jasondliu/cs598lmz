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

# The following line should not crash the interpreter.
# It should also not print anything (it would if the weakref wasn't cleared).
print(latefin.ref)
</code>
The issue is that the <code>func.__module__</code> line causes the <code>Cyclic</code> instance to be marked as reachable, and therefore its <code>__del__</code> method is not called.
The <code>Cyclic</code> instance is reachable because the <code>func</code> object has a reference to it as its <code>__module__</code> attribute.
The <code>Cyclic</code> instance is not reachable because it has a <code>__weakref__</code> slot.
The <code>Cyclic</code> instance is not reachable because it has a <code>__del__</code> method.
The <code>Cyclic</code> instance is reachable because the <code>func</code> object has a reference to it as its <code>__module__</code> attribute.
The <
