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

print(latefin.ref())
</code>
The output is:
<code>&lt;function &lt;lambda&gt; at 0x7f9f2b7a8ea0&gt;
</code>
The problem is that the <code>func</code> object is not deallocated, and it is not possible to deallocate it.
The <code>func</code> object has a reference to the <code>Cyclic</code> object, and the <code>Cyclic</code> object has a reference to the <code>LateFin</code> object, and the <code>LateFin</code> object has a reference to the <code>func</code> object.
The <code>func</code> object is a function, and functions are not deallocated.
The <code>Cyclic</code> object is a tuple, and tuples are not deallocated.
The <code>LateFin</code> object is a class instance, and class instances are not deallocated.
The <code>func</code> object has a reference to
