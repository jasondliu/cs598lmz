import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

c = C()
c.a = C()
c.a.b = c
del c

gc.collect()

# Test gc.get_referrers()

class C:
    pass

c = C()
c.a = C()
c.a.b = c

# Test gc.get_referents()

class C:
    pass

c = C()
c.a = C()
c.a.b = c

# Test gc.get_objects()

class C:
    pass

c = C()
c.a = C()
c.a.b = c

# Test gc.is_tracked()

class C:
    pass

c = C()
c.a = C()
c.a.b = c

# Test gc.set_debug()

class C:
    pass

c = C()
c.a = C()
c.a.b = c

# Test gc.get_debug()
