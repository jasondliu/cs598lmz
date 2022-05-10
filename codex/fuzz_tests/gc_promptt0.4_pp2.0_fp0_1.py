import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() collects all cyclic garbage that
# can be collected.  It's not a complete test, but it's better than
# nothing.

# Create some cyclic garbage.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

a = A()
b = B()
c = C()
a.b = b
b.a = a
b.c = c
c.b = b

# Check that they are not collected.

print(gc.collect())

# Clear the references to them.

a = b = c = None

# Check that they are collected.

print(gc.collect())

# Create some more cyclic garbage.

a = A()
b = B()
c = C()
a.b = b
b.a = a
b.c = c
c.b = b

# Check that they are not collected.

print(gc.collect())

# Clear the references to them.

a = b
