import weakref
# Test weakref.ref.

class Foo(object):
    def __init__(self, value):
        self.value = value
        self.id = id(self)

class Dummy:
    pass

def test_as_ref():
    for target in (Foo(42), None):
        ref = weakref.ref(target)
        assert ref() is target
        assert repr(ref).startswith('<weakref at 0x')
        if target is None:
            assert repr(ref) == "<weakref to None; dead>"
        else:
            assert repr(ref) == "<weakref at 0x%X; to 'Foo' at 0x%x (%r)>" % (
                                id(ref), target.id, target.value)

def test_constructor_types():
    class Subclass(weakref.ref):
        pass

    for t in [int, str, bytes, bytearray, list, dict, Foo,
              weakref.ref, Subclass]:
        raises(TypeError, t, 1, 2, 3)
