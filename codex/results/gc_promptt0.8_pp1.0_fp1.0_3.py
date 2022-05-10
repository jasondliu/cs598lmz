import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect when cycles exist in the object graph.
# See also test_gc.py for more gc-related tests.
#
# See http://www.python.org/sf/547845 for a discussion of this test.

class OldStyle:
    pass

class C:
    pass

class D:
    pass

def test_oldstyle():
    # an old-style class
    c = OldStyle()
    c.a = c
    wr = weakref.ref(c)
    d = c.__dict__
    d['b'] = c
    del c, d
    gc.collect()
    assert wr()

def test_oldstyle_two():
    # an old-style class, with two cycles
    c = OldStyle()
    c.a = c
    c.b = c
    wr = weakref.ref(c)
    d = c.__dict__
    d['c'] = c
    d['d'] = c
    del c, d
    gc.collect()
    assert wr()

def test_oldstyle
