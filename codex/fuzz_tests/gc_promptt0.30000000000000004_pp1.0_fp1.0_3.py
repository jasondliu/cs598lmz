import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

print(gc.collect())
del a
del b
print(gc.collect())
# Test gc.get_objects()
class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

print(gc.collect())
del a
del b
print(gc.collect())
print(gc.get_objects())
# Test gc.get_referrers()
class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

print(gc.collect())
del a
del b
print(gc.collect())
print(gc.get_referrers(A))
print(gc.get_referrers(B))
# Test gc.get_referents()
class A:
    pass

