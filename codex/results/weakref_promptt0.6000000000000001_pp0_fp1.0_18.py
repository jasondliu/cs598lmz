import weakref
# Test weakref.ref(x) and weakref.proxy(x)
import sys

def is_dead(wr):
    try:
        wr()
    except ReferenceError:
        return True
    else:
        return False

class Foo(object):
    pass

def test_weakref_ref():
    foo = Foo()
    foo.x = 42
    foo.y = "hello"
    foo.z = 3.5
    foo.w = [1, 2, 3]
    foo.v = (4, 5, 6)
    foo.u = {'a': 1, 'b': 2, 'c': 3}

    # test __new__
    foo_wr = weakref.ref(foo)
    assert not is_dead(foo_wr)
    assert foo_wr() is foo

    # test __call__
    assert foo_wr() is foo
    assert foo_wr().x == 42
    assert foo_wr().y == "hello"
    assert foo_wr().z == 3.5
    assert foo_wr().w == [1, 2, 3]
