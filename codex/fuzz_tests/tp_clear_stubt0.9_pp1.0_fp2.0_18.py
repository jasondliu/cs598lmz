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
several_refs_to_selfcycle = weakref.ref(latefin)
del latefin
gc.collect()
if several_refs_to_selfcycle():
    print("yes, this hooks are called")
else:
    print("Self-reference is lost, late finalliers can't be called")
</code>

