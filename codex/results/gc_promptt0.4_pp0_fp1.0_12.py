import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

a_id = id(a)
b_id = id(a.b)

del a
gc.collect()

assert gc.get_referrers(a_id) == []
assert gc.get_referrers(b_id) == []

a = A()
a.b = A()
a.b.a = a

a_id = id(a)
b_id = id(a.b)

del a
gc.collect()

assert gc.get_referrers(a_id) == []
assert gc.get_referrers(b_id) == []

# Test gc.get_referrers()

a = A()
a.b = A()
a.b.a = a

a_id = id(a)
b_id = id(a.b)

refs = gc.get_referrers(
