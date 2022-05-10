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
try:
    gc.collect()
except RuntimeError:
    pass
else:
    raise AssertionError("Didn't raise after __del__")

"""
import gc
import weakref

class Foo(object):
    pass

class TestGc(object):
    def __init__(self):
        self.foo = Foo()
        self.foo_wr = weakref.ref(self.foo)
        self.foo.foo_ref = weakref.ref(self.foo)
        self.foo.t1_ref = weakref.ref(self)
        self.foo.t2_ref = weakref.ref(self)

    def test_gc(self):
        # GC only cleanup items in one pass, so run it twice.
        gc.collect()
        gc.collect()
        
        # Test if weak reference were cleared correctly.
        self.assertEqual(self.foo_wr(), None)
        self.assertEqual(self.foo.foo_ref(), self.foo)
        self
