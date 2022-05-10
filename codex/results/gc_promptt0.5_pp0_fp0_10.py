import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

w = weakref.ref(A())

del A

print(gc.collect())
print(gc.collect())
print(w())

# Check that the weakref is gone
print(gc.collect())
print(gc.collect())
print(w())
