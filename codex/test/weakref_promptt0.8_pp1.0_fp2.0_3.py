import weakref
# Test weakref.ref() on built-in function types
import _weakref
import operator

basemeth = type.__repr__

class Meta(type):
    def __repr__(self):
        return "meta"

class C(metaclass=Meta):

    def meth(self, x, y):
        return self, x, y

    @classmethod
    def cmeth(cls, x, y):
        return cls, x, y

    @staticmethod
    def smeth(x, y):
        return x, y

class D(C):
    pass

def test_basic():
    f = C().meth
    f(1, 2)
    wr = weakref.ref(f)
    f = None
    assert wr() is None
    f = D().meth
    wr = weakref.ref(f)
    f = None
    assert wr() is None

def test_builtin():
    f = operator.floordiv
    wr = weakref.ref(f)
    f = None
    assert wr() is None
