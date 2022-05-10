import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Create a bunch of objects that refer to each other in various ways.
# Call gc.collect() and check that everything gets collected.
#
# This test is not as thorough as it could be, but it's a start.

# Create a bunch of objects that refer to each other in various ways.

class A:
    pass

a = A()
a.a = a

b = A()
b.a = a
b.b = b

c = A()
c.a = a
c.b = b
c.c = c

d = A()
d.a = a
d.b = b
d.c = c
d.d = d

e = A()
e.a = a
e.b = b
e.c = c
e.d = d
e.e = e

f = A()
f.a = a
f.b = b
f.c = c
f.d = d
f.e = e
f.f = f

g = A()
g.a = a

