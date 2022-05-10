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

# ____________________________________________________________


def test_getattr_tricky_case():
    class X(object):
        def __getattr__(self, name):
            pass
    assert X().__dict__ is None

def test_getattribute_tricky_case():
    class X(object):
        def __getattribute__(self, name):
            pass
    assert X().__dict__ is None

def test_getattribute_and_getattr():
    class X(object):
        def __getattr__(self, name):
            return 'getattr'
        def __getattribute__(self, name):
            return 'getattribute'
    x = X()
    assert x.foo == 'getattr'
    assert x.__dict__ == 'getattr'

def test_class_setattr():
    class X(object):
        def __getattr__(self, name):
            return 'getattr'
        def __getattribute__(self, name):
            return 'getattribute'
    X.foo = 'foo'
