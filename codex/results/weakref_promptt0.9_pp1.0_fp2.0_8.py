import weakref
# Test weakref.ref() on subclasses of int and long.
# Also test calling unbound methods.

# This custom __hash__ is needed to support identity-based hashing
# in Python 3.  We may need to use a custom __eq__, too.
class IntSubclass(int):
    def __hash__(self):
        return int.__hash__(self)


class LongSubclass(long):
    def __hash__(self):
        return long.__hash__(self)

class TestWeakref:

    def test_intsubclass(self):
        o = IntSubclass(1)
        assert o == 1
        r = weakref.ref(o)
        assert r() == o
        assert r == o
        assert r() == 1

    def test_longsubclass(self):
        o = LongSubclass(1L)
        assert o == 1L
        r = weakref.ref(o)
        assert r() == o
        assert r == o
        assert r() == 1L

    def test_basic(self):
        class C(object):
           
