import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

c = C()
c.x = C()
c.y = [C()]
c.z = weakref.ref(c)

print(gc.collect())
print(gc.collect())
print(gc.collect())

# Test gc.garbage

class C:
    pass

c = C()
c.x = C()
c.y = [C()]
c.z = weakref.ref(c)

print(gc.collect())
print(gc.garbage)

# Test gc.get_count()

print(gc.get_count())

# Test gc.get_debug()

print(gc.get_debug())

# Test gc.get_objects()

print(len(gc.get_objects()))

# Test gc.get_referrers()

print(len(gc.get_referrers(gc)))

# Test gc.get_threshold()

print(gc.get_threshold())

# Test g
