import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print "in bar"

f = Foo()
f.x = bar
f.x()

del f

gc.collect()

# Test gc.garbage

class Foo:
    pass

def bar():
    print "in bar"

f = Foo()
f.x = bar
f.x()

del f

gc.garbage.append(Foo())
gc.garbage.append(Foo())

gc.collect()

# Test gc.get_debug()

gc.get_debug()

# Test gc.get_objects()

gc.get_objects()

# Test gc.get_referrers()

gc.get_referrers(gc)

# Test gc.get_threshold()

gc.get_threshold()

# Test gc.is_tracked()

gc.is_tracked(gc)

# Test gc.set_debug()

gc.set_debug(gc.
