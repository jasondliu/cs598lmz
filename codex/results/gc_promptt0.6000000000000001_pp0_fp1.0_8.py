import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
a = weakref.ref(None)
print(gc.collectable())
print(gc.collectable(a))
print(gc.collectable(a))
print(gc.collectable(a))

# Test gc.get_referrers()
a = weakref.ref(None)
print(gc.get_referrers(a))
print(gc.get_referrers(a))
print(gc.get_referrers(a))

# Test gc.get_referents()
a = weakref.ref(None)
print(gc.get_referents(a))
print(gc.get_referents(a))
print(gc.get_referents(a))


# Test gc.get_objects()
a = weakref.ref(None)
print(gc.get_objects())
print(gc.get_objects())
print(gc.get_objects())

# Test gc.get_count()
print(gc.get_count())
print(gc.get_count())
print(gc
