import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    o = Foo()
    o.x = o
    o.y = o
    o.z = o
    return o

def test():
    o = bar()
    o = None
    gc.collect()

test()

# Test gc.get_referrers()

def test():
    o = bar()
    r = gc.get_referrers(o)
    assert len(r) == 1
    assert r[0] is o
    o = None
    gc.collect()

test()

# Test gc.get_referents()

def test():
    o = bar()
    r = gc.get_referents(o)
    assert len(r) == 3
    assert o.x in r
    assert o.y in r
    assert o.z in r
    o = None
    gc.collect()

test()

# Test gc.get_objects()

def test():
    o =
