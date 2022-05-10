import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Test whether an object is garbage collected

# In python, objects are garbage collected when they lose their reference
# When the ref count of an object drops to zero
# When an object has no reference cycle

a = [1, 2, 3]
b = a
del a

print(b)

# gc.collect()
try:
    print(a)
except NameError:
    print("Error: a is deleted")

# gc.get_stats()
# gc.get_threshold()

# gc.enable()
# gc.disable()

# gc.set_debug(gc.DEBUG_STATS)
# gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# gc.get_referrers()
# gc.get_referents()

# gc.is_tracked()
# gc.set_track_types()

a = {}
b = [a]
print(gc.is_tracked(a))
print(gc.is_tracked(b))

gc
