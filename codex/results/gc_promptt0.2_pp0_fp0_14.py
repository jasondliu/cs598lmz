import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    c.x = c
    c.y = C()
    c.y.x = c
    del c

f()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_referrers()

def f():
    c = C()
    c.x = c
    c.y = C()
    c.y.x = c
    return c

c = f()
r = gc.get_referrers(c)
assert len(r) == 3
assert c in r
assert r[1] is r[2]
assert r[1][0] is c
assert r[1][1] is c.y
assert r[1][2] is c.y.x

# Test gc.get_referents()

r = gc.get_referents(c)
assert len(r) == 3
assert c in r
assert c.x in r
assert c
