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

# the next line is the problem:
func()
</code>
The problem is that the <code>LateFin</code> object is destroyed, but the <code>Cyclic</code> object is not, and it is not even put in the unreachable list.
I tried to reproduce the problem in a simpler way, but I couldn't.
The problem is that the <code>Cyclic</code> object is not destroyed, and so the <code>LateFin</code> object is not destroyed, and so the function is not destroyed, and so the module is not destroyed.
I tried to reproduce the problem in a simpler way, but I couldn't.

