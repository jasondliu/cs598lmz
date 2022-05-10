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

expected = "referencing LateFin.__del__ from weakly-referenced Cyclic"
assert weakref.getweakrefcount(latefin) == 1
assert weakref.getweakrefs(latefin)
try:
    pickle.dumps(latefin)
except Exception as e:
    print(e)
    assert str(e).startswith(expected)
else:
    raise Exception("Expected an exception")

# cleanup
del weakref.getweakrefs, weakref.getweakrefcount, latefin
