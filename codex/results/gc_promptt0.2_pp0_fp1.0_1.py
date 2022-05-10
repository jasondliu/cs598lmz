import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a

del a, b

gc.collect()

# Test gc.get_referrers()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a

del a, b

gc.collect()

print gc.get_referrers(A)

# Test gc.get_objects()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a

del a, b

gc.collect()

print gc.get_objects()

# Test gc.get_referents()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a

del a, b

gc.collect()

print gc.get_referents(A)

#
