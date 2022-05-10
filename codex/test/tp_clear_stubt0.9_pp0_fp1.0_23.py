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
del func, cyc, LateFin
while gc.collect():
    pass
try:
    f = func.__module__
except NameError:
    pass
else:
    raise Exception("func was not cleared.")
tmp = latefin.ref()
del latefin
while gc.collect():
    pass

# Issue #18771: test that the cyclic gc does not segfault on an eager custom dict.
# Issue #19092: test that the cyclic gc does not hang on an eager custom dict
# with a kwds__getitem__ slot.
if not gc.isenabled():
    tmp = None

class EagerDict:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __getitem__(self, key):
        return self.__dict__[key]

    def __del__(self):
        pass

eager_dict = EagerDict(
    item1=1,
    item2=2,
    item3=3,
)

gc.disable()

