import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C(object):
    pass

class D(object):
    pass

def f():
    c = C()
    d = D()
    c.d = d
    d.c = c
    del c, d

f()
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_objects()

# Test gc.get_referrers()

# Test gc.get_referents()

# Test gc.get_threshold()

# Test gc.set_threshold()

# Test gc.get_count()

# Test gc.is_tracked()

# Test gc.set_debug()

# Test gc.is_enabled()

# Test gc.disable()

# Test gc.enable()

# Test gc.isenabled()

# Test gc.collect()

# Test gc.get_debug()

# Test gc.set_debug()

# Test gc.get_threshold()

