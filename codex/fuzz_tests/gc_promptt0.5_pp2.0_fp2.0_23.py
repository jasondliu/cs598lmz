import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
c = A()
c.b = b
b.c = c
a.c = c
del a
del b
del c
gc.collect()

# Test gc.get_referrers()
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
c = A()
c.b = b
b.c = c
a.c = c
del a
del b
del c
gc.collect()
assert gc.get_referrers(A) == [{'__builtins__': __builtins__}]

# Test gc.get_objects()
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
c = A()
c.b = b
b.c = c
a.c = c
del a
del b
del c
gc.collect()
assert gc
