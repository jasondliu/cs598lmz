import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C:
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a

del a
del b

gc.collect()

print(gc.collect())

# Test gc.get_objects()

class A:
    pass

class B:
    pass

class C:
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a

del a
del b

gc.collect()

print(gc.get_objects())

# Test gc.get_referrers()

class A:
    pass

class B:
    pass

class C:
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a

del a
del b

gc.collect()

print(gc.get_referrers(C))
