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

f = None
gc.collect()
print(latefin.ref() is None) # False
</code>
From what I understand, when <code>del func</code> happens, <code>func</code> should be set to <code>None</code>, not destroyed, because it is part of the module <code>cyc</code>. Likewise, when <code>del cyc</code> happens, only <code>cyc[1]</code> should be destroyed, and <code>cyc[0]</code> should be set to <code>None</code>. Afterwards, when <code>latefin.ref() is None</code> happens, <code>latefin.ref</code> should certainly be alive, but <code>latefin.ref()</code> should be <code>None</code>.
However, what this prints is <code>False</code>! It seems like <code>del cyc</code> doesn't set <code>cyc[0]</code> to <code>None</code>, but instead destroys it too!
Why is this program printing <code>False</
