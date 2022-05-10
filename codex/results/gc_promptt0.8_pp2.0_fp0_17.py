import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a non-collectable object.
a = []
a.append(a)
b = gc.collect()
assert b == 0
assert gc.is_tracked(a)

# Test gc.collect() with a collectable object.
c = []
a.append(c)
b = gc.collect()
assert b == 1
assert gc.is_tracked(c)
assert not gc.is_tracked(a)
del a
b = gc.collect()
assert b == 1

# Test gc.collect() with a collectable object, with a circular
# reference to itself.
class Foo:
    pass

a = Foo()
a.b = a
b = gc.collect()
assert b == 1
assert not gc.is_tracked(a)
del a
b = gc.collect()
assert b == 1

# Test a corner case.  The bug was that, when collect_generations()
# is called, the next collection of objects whose generation number
# is lower than the one being collected is triggered if
