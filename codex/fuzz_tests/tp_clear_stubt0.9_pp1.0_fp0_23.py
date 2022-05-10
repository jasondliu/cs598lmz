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

if weakref.getweakrefcount(latefin) != 1:
    raise TestFailed("cyclic garbage not collected")
if weakref.getweakrefcount(latefin.ref) != 1:
    raise TestFailed("weakref to cyclic garbage not collected")
if latefin.ref() is not None:
    raise TestFailed("weakref to cyclic garbage at %x not None")

#=======================================================================
# Make sure that subclasses of weakref objects are garbage collected
#  immediately after the weakref reference goes out of scope.
#=======================================================================

class X(object):
    pass

def gc_collect():
    func = gc.collect
    func()
    return func

class Y(weakref.ref):
    def __del__(self):
        self._co = gc_collect()

def func():
    return None

def run():
    # This makes sure that the weakref.ref subclass Y has a __del__.
    # Otherwise the bug is masked.
    for i in range(1000):
