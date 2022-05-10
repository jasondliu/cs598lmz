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
gc.collect()       # break a strong reference loop and
                   # increment the garbage-collectable count

try:
    del latefin
except TypeError:
    pass
else:
    raise SystemError("cleaning up the cyclic object didn't fail")

# Try that again, but this time use an uncollectable callback,
# and verify that a second collection pass doesn't freak out.

class CyclicCantCollect(tuple):
    __slots__ = ()
    def __del__(self):
        global dont_collect
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(CyclicCantCollect, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

dont_collect = []
try:
    del latefin
except TypeError:
    pass
else:
    raise SystemError("cleaning up the cyclic object didn't fail
