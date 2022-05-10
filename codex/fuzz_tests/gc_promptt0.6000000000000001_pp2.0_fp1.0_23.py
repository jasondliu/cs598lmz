import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
id(a), id(b)

a_id = id(a)
b_id = id(b)

del a, b
gc.collect()

print(gc.garbage)

# Test gc.collect()
class A:
    pass

a = A()
b = A()
id(a), id(b)

a_id = id(a)
b_id = id(b)

a.b = b
b.a = a

del a, b
gc.collect()

print(gc.garbage)
# Test gc.is_tracked()
class A:
    pass

a = A()
b = A()
id(a), id(b)

a_id = id(a)
b_id = id(b)

a.b = b
b.a = a

del a, b
gc.collect()

print(gc.is_tracked(gc.garbage[0]))
