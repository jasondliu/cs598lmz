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
</code>
It results in:
<code>Exception ignored in: &lt;function LateFin.__del__ at 0x7f4d4f1b4c80&gt;
Traceback (most recent call last):
  File "&lt;input&gt;", line 10, in __del__
AttributeError: 'LateFin' object has no attribute 'ref'
</code>
What happens is that the <code>LateFin</code> instance is destroyed first, and then the <code>Cyclic</code> instance. The <code>__del__</code> method of <code>Cyclic</code> tries to update the <code>ref</code> attribute of <code>LateFin</code>, which no longer exists.
<code>del func, cyc</code> is used to make sure that the objects are not reachable anymore, so that the garbage collector will collect it.

