import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    c.x = c
    del c

f()
gc.collect()

# Test gc.get_referrers()

def f():
    c = C()
    c.x = c
    return c

c = f()
r = gc.get_referrers(c)
assert len(r) == 2
assert r[0] is c
assert r[1] is globals()

# Test gc.get_referents()

r = gc.get_referents(c)
assert len(r) == 2
assert r[0] is c
assert r[1] is c

# Test gc.get_objects()

r = gc.get_objects()
assert len(r) >= 3
assert c in r
assert f in r
assert C in r

# Test gc.is_tracked()

assert gc.is_tracked(c)
assert gc.is_tracked(f)
