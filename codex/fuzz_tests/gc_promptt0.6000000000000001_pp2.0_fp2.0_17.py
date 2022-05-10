import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    g = [weakref.ref(x) for x in range(10)]
    print gc.collect()

f()

# Test gc.garbage

class A:
    pass

class B(A):
    pass

del A

x = B()
del B

gc.collect()

assert len(gc.garbage) == 1

# Test gc.get_count()

assert gc.get_count() == (7, 7, 7)

# Test gc.set_threshold()

gc.set_threshold(1000)
assert gc.get_threshold() == (1000, 1000, 1000)

gc.set_threshold(*gc.get_threshold())
assert gc.get_threshold() == (1000, 1000, 1000)

gc.set_threshold(100, 200, 300)
assert gc.get_threshold() == (100, 200, 300)

# Test gc.get_objects()

assert len(gc.get_objects()) ==
