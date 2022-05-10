import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference graph
a.y = a
b.y = b
c.y = c
d.y = d

# Create a reference tree
a.z = b
b.z = c
c.z = d
d.z = a

# Create a reference graph
a.w = a
b.w = b
c.w = c
d.w = d

# Create a reference tree
a.v = b
b.v = c
c.v = d
d.v = a

# Create a reference graph
a.u = a
b.u = b
c.u = c
d.u = d

# Create a reference tree
