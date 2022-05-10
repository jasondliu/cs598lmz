import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test used to fail because `a` was in a cycle, and the
# gc didn't notice that `a` was collectable.

a = []
a.append(a)
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.
