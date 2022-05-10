import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
b = a.b
# a and b are collectable

gc.collect()

# a and b are uncollectable
a.b = 42
a.b = b
b.a = a
# a and b are collectable

gc.collect()

# a and b are uncollectable
a.b = 42
a.b = b
b.a = a
# a and b are collectable

del a, b
gc.collect()

# a and b are collectable
a = A()
a.b = A()
a.b.a = a
b = a.b
# a and b are collectable

gc.collect()

# a and b are uncollectable
a.b = 42
a.b = b
b.a = a
# a and b are collectable

# a and b are uncollectable
a.b = 42
a.b = b
b.a = a
# a
