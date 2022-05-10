import weakref
# Test weakref.ref() doesn't crash if called inside a try-except block
try:
    weakref.ref(int)
except TypeError:
    pass


def test_weakref_del():
    class Foo:
        pass

    foo = Foo()
    wr = weakref.ref(foo)
    del foo
    assert wr() is None


def test_weakref_call():
    class Foo:
        pass

    foo = Foo()
    wr = weakref.ref(foo)
    assert wr() == foo

def test_weakref_iter():
    class Foo:
        pass

    foo1 = Foo()
    foo2 = Foo()
    foo3 = Foo()

    wr1 = weakref.ref(foo1)
    wr2 = weakref.ref(foo2)
    wr3 = weakref.ref(foo3)

    assert {wr1, wr2, wr3} == {wr1, wr2, wr3}
    assert {wr1, wr2, wr3} == {wr1, wr3, wr2}
