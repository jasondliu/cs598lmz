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
rcnt = gc.collect()
if len(gc.garbage) != 1:
    print('skipped')
    raise SystemExit

# test for a corner case in the weakref implementation
# where it used to call the __del__ of the referenced object
# while the weakref was still in an inconsistent state
class X:
    __slots__ = ('ref')
    def __init__(self, x=None):
        self.ref = x
    def __del__(self):
        global func
        func = self.ref

# generate two instances of X and trigger a call to __del__
del x, y
x = X()
y = X(x)
del x
rcnt = gc.collect()

# and now the real stuff
# in the original bug, this would raise an exception
# because the object was not fully initialized
if func is None:
    print('skipped')
    raise SystemExit
func()
