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
del func, cyc, latefin

gc.collect()
</code>
Running it (with Python 3.3.3) gives:
<code>Traceback (most recent call last):
  File "crash.py", line 18, in &lt;module&gt;
    gc.collect()
  File "crash.py", line 15, in &lt;module&gt;
    del latefin
AttributeError: 'LateFin' object has no attribute 'ref'
</code>
In this example, the <code>LateFin</code> instance was destroyed before its <code>ref</code> attribute got set. Obviously this is a contrived example, but I believe it indicates that there is a race condition in the GC.
A race condition would mean that there is no guarantee as to finalizer order, so we have to be careful not to have dependencies on other objects' finalizers as in this example.
I would be interested in knowing if this is an actual race condition in CPython (as opposed to a bug in 3.3.3) and if it applies to Python 2.x as well.


A:

Yes, there's
