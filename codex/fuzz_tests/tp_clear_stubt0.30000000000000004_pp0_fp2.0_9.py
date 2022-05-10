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

# This is a test for a bug in the implementation of weakrefs:
# the callback for a weakref was called while the weakref still
# existed, and the callback would then try to look up the weakref
# in the list of weakrefs of the object.  This would fail, and
# would put the weakref in an invalid state.

import gc, weakref

class A:
    pass

class B(A):
    pass

def callback(ref):
    ref.__class__

a = A()
b = B()
b.a = a
a.b = b

a_ref = weakref.ref(a, callback)
b_ref = weakref.ref(b, callback)
del a, b
gc.collect()

# This is a test for a bug in the implementation of weakrefs:
# the callback for a weakref was called while the weakref still
# existed, and the callback would then try to look up the weakref
# in the list of weakrefs of the object.  This would fail,
