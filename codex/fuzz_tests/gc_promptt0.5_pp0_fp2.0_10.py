import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print("Collecting...")
n = gc.collect()
print("Unreachable objects:", n)
print("Remaining garbage:", end=" ")
print(gc.garbage)

# Test gc.garbage
print("Collecting...")
n = gc.collect()
print("Unreachable objects:", n)
print("Remaining garbage:", end=" ")
print(gc.garbage)

# Test weakref.ref()
print("Creating cycles...")
a = {}; b = {}; c = {}
a['b'] = b; b['a'] = a
del a, b
print("Collecting...")
n = gc.collect()
print("Unreachable objects:", n)
print("Remaining garbage:", end=" ")
print(gc.garbage)
