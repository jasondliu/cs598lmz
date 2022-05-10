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
    del c

f()
gc.collect()

# Test gc.get_objects()

class C:
    pass

def f():
    c = C()
    c.x = c
    del c

f()
gc.collect()

# Test gc.get_referents()

class C:
    pass

def f():
    c = C()
    c.x = c
    del c

f()
gc.collect()

# Test gc.get_threshold()

gc.get_threshold()

# Test gc.get_count()

gc.get_count()

# Test gc.set_threshold()

gc.set_threshold(
