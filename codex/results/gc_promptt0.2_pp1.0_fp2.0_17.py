import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

l = gc.get_referrers(a)
print(l)
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

l = gc.get_referrers(a)
print(l)
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

l = gc.get_referrers(a)
print(l)
del a
gc.collect()
# Test gc.get_referrers()
class
