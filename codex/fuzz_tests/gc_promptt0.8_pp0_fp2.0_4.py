import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Create a few objects with a cycle.  Check that we can break the cycle
# with gc.collect().

class A:
    pass

class B(A):
    pass

# First try: a reference loop
a = A()
a.b = B()
a.b.a = a
del a
gc.collect()

# Second try: a reference ladder
a = A()
a.b = B()
a.b.a = A()
a.b.a.b = a.b
del a
gc.collect()

# Third try: a reference net
a = A()
a.b = B()
a.b1 = B()
a.b.a = a
a.b1.a = a
del a
gc.collect()

# Fourth try: a more complex net (attributes whose name is an integer)
# The number 42 is used because the random choice of attributes names
# with attribute cache (see structmember.c)
a = A()
a.b = B()
a.b1 = B()
for
