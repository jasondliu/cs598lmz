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
Is it okay to access the <code>ref</code> attribute of the object after object deletion (does it mean object has been yet cleared from the heap)?
Is not it a bug that finalizer triggers a script crash?
Note:
I've found that the cause of this problem is the line <code>del latefin</code> in the finalizer.
If I don't delete the object it doesn't crash.
However I can still access the object through a weak reference after the finalizer was called.
Should I have access to the object through the weak reference after its finalizer was called?
Python versions:

Python 3.7.0 x64
Python 3.6.5 x64
Python 3.6.4 x32
Python 3.5.3 x64

Result: the same

