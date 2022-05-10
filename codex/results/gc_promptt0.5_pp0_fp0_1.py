import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    a = []
    a.append(a)
    del a
    gc.collect()
    print('ok')
f()

# Test gc.garbage
class A:
    pass
gc.collect()
print(gc.garbage)

# Test gc.get_objects()
class A:
    pass
gc.collect()
print(len(gc.get_objects()))

# Test gc.get_referrers()
class A:
    pass
gc.collect()
print(len(gc.get_referrers(A)))

# Test gc.get_referents()
class A:
    pass
gc.collect()
print(len(gc.get_referents(A)))

# Test gc.is_tracked()
class A:
    pass
gc.collect()
print(gc.is_tracked(A()))

# Test gc.set_threshold()
gc.set_threshold(1)
gc.collect()
gc.set_threshold(10
