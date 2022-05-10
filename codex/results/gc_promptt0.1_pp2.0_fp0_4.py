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

class C:
    pass

def f():
    c = C()
    c.x = c
    return c

c = f()
r = gc.get_referrers(c)
assert len(r) == 2
assert r[0] is c
assert r[1] is c.__dict__

# Test gc.get_referents()

class C:
    pass

def f():
    c = C()
    c.x = c
    return c

c = f()
r = gc.get_referents(c)
assert len(r) == 2
assert r[0] is c
assert r[1] is c.__dict__

# Test gc.get_objects()

class C:
    pass

def f():
    c = C()
    c
