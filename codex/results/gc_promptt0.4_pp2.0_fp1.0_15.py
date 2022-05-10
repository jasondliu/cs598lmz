import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    pass

f = Foo()
f.x = f
print gc.collect()

# Test gc.get_referrers()
a = []
b = [a]
a.append(b)

print gc.get_referrers(a)
print gc.get_referrers(b)

# Test gc.get_referents()
print gc.get_referents(a)
print gc.get_referents(b)

# Test gc.get_objects()
print len(gc.get_objects())

# Test gc.is_tracked()
print gc.is_tracked(a)
print gc.is_tracked(b)

# Test gc.garbage
print len(gc.garbage)

# Test gc.get_stats()
print gc.get_stats()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG
