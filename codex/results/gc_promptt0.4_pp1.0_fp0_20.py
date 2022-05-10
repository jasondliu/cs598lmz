import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

def f():
    a = []
    a.append(a)
    del a

f()
gc.collect()

# Test gc.get_referrers()
gc.collect()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
assert gc.get_referrers(c) == [{'c': c}]

# Test gc.get_objects()
gc.collect()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
assert gc.get_objects() == [c, {'c': c}]

# Test gc.get_referents()
gc.collect()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
assert gc.get_referents(c) == [c, [c]]

# Test gc.get_threshold()
gc.collect()
a =
