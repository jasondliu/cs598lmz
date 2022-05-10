import weakref
# Test weakref.ref() on a built-in type.


class A(object):

    def __init__(self):
        self.ref = weakref.ref(float)
        self.ref2 = weakref.ref(self)


def test_weakref_on_builtin():
    a = A()
    assert a.ref() is float
    assert a.ref2() is a


def test_weakref_callable():
    class A(object):
        pass

    a = A()
    a.meth = lambda : 1
    ref = weakref.ref(a.meth)
    assert ref()() == 1


def test_weakref_dict():
    a = A()
    a.__dict__ = dict(x=42)
    ref = weakref.ref(a.__dict__)
    assert ref() == dict(x=42)


class A(object):

    def __init__(self):
        self.ref = weakref.ref(self)


def test_weakref_compare():
    a = A()
    b =
