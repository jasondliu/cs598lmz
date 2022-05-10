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
del latefin


# ____________________________________________________________

def test_gc_implicit_cycles(self):
    import gc, weakref

    class C:
        pass

    class D:
        pass

    def f():
        pass

    def g():
        pass

    def h():
        pass

    # Create a cycle.
    c = C()
    c.foo = c
    wr = weakref.ref(c)
    del c

    # Check that the cycle gets collected.
    gc.collect()
    self.assert_(wr() is None)

    # Check that globals with cyclic dependencies are collected.
    C.foo = D()
    D.foo = C()
    gc.collect()
    self.assert_(wr() is None)

    # Check that a global with a dependency to a local can be collected.
    C.foo = f
    f.foo = C
    gc.collect()
    self.assert_(wr() is None)

    # Check that a global with a dependency to a free variable can be
