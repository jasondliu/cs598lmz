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

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = a

# Create a reference cycle
