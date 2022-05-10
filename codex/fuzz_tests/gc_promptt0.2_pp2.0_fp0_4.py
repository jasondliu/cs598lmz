import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()

a.b = b
b.a = a

del a
del b

gc.collect()

# Test gc.garbage

class A:
    pass

class B:
    pass

a = A()
b = B()

a.b = b
b.a = a

del a
del b

gc.collect()

# Test gc.get_objects()

class A:
    pass

class B:
    pass

a = A()
b = B()

a.b = b
b.a = a

del a
del b

gc.collect()

# Test gc.get_referrers()

class A:
    pass

class B:
    pass

a = A()
b = B()

a.b = b
b.a = a

del a
del b

gc.collect()

# Test gc.get_referents()

class A
