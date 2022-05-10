import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()

print(gc.collect())

del a

print(gc.collect())

# Test gc.get_objects()

class A:
    pass

a = A()

print(gc.get_objects())

del a

print(gc.get_objects())

# Test gc.get_count()

print(gc.get_count())

# Test gc.get_stats()

print(gc.get_stats())

# Test gc.get_threshold()

print(gc.get_threshold())

# Test gc.set_threshold()

print(gc.set_threshold(0, 0, 0))

# Test gc.is_tracked()

class A:
    pass

a = A()

print(gc.is_tracked(a))

del a

print(gc.is_tracked(a))

# Test gc.set_debug()

print(gc.set_debug(
