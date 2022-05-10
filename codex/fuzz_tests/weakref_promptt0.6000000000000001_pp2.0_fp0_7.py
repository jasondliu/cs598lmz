import weakref
# Test weakref.ref()
import sys
import weakref

class Foo:
    pass

def bar():
    pass

def test_weakref_ref():
    # Test weakref.ref()
    f = Foo()
    wr = weakref.ref(f)
    assert wr() is f
    assert wr().__class__ is Foo
    del f
    assert wr() is None
    f = Foo()
    wr = weakref.ref(f)
    assert wr() is f
    assert wr().__class__ is Foo
    f.attr = 42
    assert wr().attr == 42
    class SubFoo(Foo):
        pass
    sf = SubFoo()
    wr = weakref.ref(sf)
    assert wr() is sf
    assert wr().__class__ is SubFoo
    del sf
    assert wr() is None
    sf = SubFoo()
    wr = weakref.ref(sf)
    assert wr() is sf
    assert wr().__class__ is SubFoo
    sf.attr = 42
    assert wr().
