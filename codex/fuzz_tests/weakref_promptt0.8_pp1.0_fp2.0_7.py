import weakref
# Test weakref.ref
from test import test_support
from test.test_support import run_with_locale

class C:
    pass

def f():
    pass

def g():
    pass

def test_hash():
    c = C()
    x = c.__hash__ = 5
    assert hash(c) == 5
    del c.__hash__
    assert hash(c) == id(c)

    c = C()
    c.__hash__ = lambda y: 42
    assert hash(c) == 42
    del c.__hash__

    try:
        hash(c)
    except TypeError:
        pass
    else:
        raise AssertionError

    # bug 858600 -- hash of weakref to hashable object should be hash of object
    # https://sourceforge.net/tracker/?func=detail&atid=105470&aid=858600&group_id=5470
    class C:
        def __init__(self, x):
            self.x = x
        def __hash__(self):
            return
