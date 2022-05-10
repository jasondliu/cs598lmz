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

'''

# ____________________________________________________________

def test_weakref_to_const_string():
    # Hack needed for PyPy, because it needs to store the weakrefs
    # to the const strings in a data structure, and that is not
    # possible if the strings are const.  There is no harm in doing
    # this hack for CPython too, it just doesn't need it.
    import weakref
    def f():
        return 'x'
    x = f()
    x += 'y'
    r = weakref.ref(x)
    x += 'z'
    assert r() == 'xyz'

# ____________________________________________________________

def test_weakref_to_freed_memory():
    import weakref
    class X(object):
        pass
    x = X()
    x.foo = 42
    x.bar = "xxx"
    del x
    #
    import gc; gc.collect()
    #
    for i in range(200):
        gc.collect()
        y
