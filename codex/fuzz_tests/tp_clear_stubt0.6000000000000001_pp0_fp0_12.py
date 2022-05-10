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
del func, cyc, LateFin, Cyclic
gc.collect()

from gc import get_referrers
print(get_referrers(latefin))
</code>
This produces <code>&lt;weakref at 0x1097c5f08; to 'function' at 0x1097c5ea0&gt;</code> on my machine (Python 3.5.2 on OSX 10.12.6).
The trick here is that we get a cyclic reference between <code>func</code> and <code>cyc</code>, but when <code>cyc</code> gets collected, it is replaced with a <code>weakref</code> to <code>func</code>, so the cyclic reference stops existing.

