import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print("collecting")
n = gc.collect()
print("unreachable",n)
print("done")

# Test gc.garbage
a = []
print("collecting")
n = gc.collect()
print("unreachable",n)
print("garbage",gc.garbage)
print("done")

# Test gc.get_referrers
a = []
print("collecting")
n = gc.collect()
print("unreachable",n)
print("garbage",gc.garbage)
print("done")
print(gc.get_referrers(gc))

# Test gc.get_referents
a = []
print("collecting")
n = gc.collect()
print("unreachable",n)
print("garbage",gc.garbage)
print("done")
print(gc.get_referents(gc))

# Test gc.get_threshold
print("threshold",gc.get_threshold())

# Test gc.is_tracked
a =
