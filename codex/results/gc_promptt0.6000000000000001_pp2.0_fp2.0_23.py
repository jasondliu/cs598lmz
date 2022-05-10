import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass
for i in range(10):
    x = C()
    x.a = C()
    x.b = C()
    x.a.x = x
    x.b.y = x.a
    del x
gc.collect()

# Test gc.garbage
class C:
    pass
class D:
    pass
d = D()
d.c = C()
gc.garbage.append(d)
gc.collect()
print len(gc.garbage)

# Test gc.get_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.get_debug()

# Test gc.get_count()
for i in range(2):
    gc.get_count()

# Test gc.get_objects()
len(gc.get_objects())

# Test gc.get_referrers()
gc.get_referrers(gc)

# Test gc.get_threshold()
gc.get_threshold()

# Test g
