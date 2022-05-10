import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
a.a = A()
a.a.a = a

ref = weakref.ref(a)
del a
gc.collect()
assert ref() is None
# Test gc.garbage
class A:
    pass

def f(x):
    pass

a = A()
a.a = A()
a.a.a = a
a.a.b = f

gc.collect()
assert len(gc.garbage) == 1
# Test gc.get_count()
assert len(gc.get_count()) == 3
# Test gc.get_threshold()
assert len(gc.get_threshold()) == 3
# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
assert gc.get_threshold() == (1, 2, 3)
# Test gc.is_tracked()
class A:
    pass

a = A()
assert gc.is_tracked(a)
# Test gc
