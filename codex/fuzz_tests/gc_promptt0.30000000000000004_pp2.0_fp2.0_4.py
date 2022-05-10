import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print "callback", wr

f = Foo()
wr = weakref.ref(f, callback)
print wr

del f
gc.collect()

# Test gc.garbage

gc.garbage.append(f)
gc.collect()

# Test gc.get_objects()

print gc.get_objects()

# Test gc.get_referrers()

print gc.get_referrers(gc)

# Test gc.get_referents()

print gc.get_referents(gc)

# Test gc.set_debug()

gc.set_debug(gc.DEBUG_STATS)
gc.collect()

gc.set_debug(gc.DEBUG_LEAK)
gc.collect()

gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()

gc.set_debug(
