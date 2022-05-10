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

# Force the creation of a weakref to the function.
# This should not crash.
weakref.ref(latefin)

gc.collect()

class A:
    __slots__ = ('x', 'y')
    def __init__(self):
        self.x = 1
        self.y = 2

a = A()
a.x = a
del a
gc.collect()

# Test that the weakref callback is called with the right argument.

ref = weakref.ref(A())

def callback(arg):
    assert arg is ref(), "weakref callback not called with the right argument"

ref.callback = callback
del ref
gc.collect()


# Test that the weakref callback is called even if the referent is
# currently being finalized.


class C:
    __slots__ = ('x',)
    def __init__(self):
        self.x = 1
    def __del__(self):
        global x
        x = self.x

class D:
    __slots__ = ('y',
