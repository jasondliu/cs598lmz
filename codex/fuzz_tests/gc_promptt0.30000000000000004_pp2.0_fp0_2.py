import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

print gc.collectable()

del a

print gc.collectable()

# Test gc.get_referrers()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

print gc.get_referrers(a)

del a

print gc.get_referrers(A)

# Test gc.get_referents()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

print gc.get_referents(a)

del a

print gc.get_referents(A)

# Test gc.get_objects()

class A:
    pass

a = A()
a.b = A()
a.b.a = a

print gc.get_objects()

del a
