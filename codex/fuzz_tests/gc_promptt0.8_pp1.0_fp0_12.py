import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
a = []
# a is not collectable
b = [a, a]
# a is collectable
c = []

del a
gc.collect()

a = weakref.ref(b)
del b
gc.collect()

# Weakrefs are not collectable
b = []
b.append(a)
del a
gc.collect()

a = weakref.ref(c)
del c
gc.collect()
# c should be collectable
gc.collect()
# a is collectable
del a
gc.collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()

a = [1, 2, 3]
a = None
# 'a' is now collectable
gc.collect()

gc.set_debug(0)
gc.collect()

# At this point, b should have been collected.
# We can't directly check the object still exists, but we can
# check if the object's methods still exist.
try:
    b[0]
except Type
