import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

# Create a reference cycle
a.x = b
b.x = c
c.x = d
d.x = e
e.x = a

# Create a reference cycle with weakrefs
a.y = weakref.ref(b)
b.y = weakref.ref(c)
c.y = weakref.ref(d)
d.y = weakref.ref(e)
e.y = weakref.ref(a)

# Create a reference cycle with a weakref at the end
a.z = b
b.z = c
c.z = d
d.z = e
e.z = weakref.ref(a)

# Create a reference cycle with a weakref at the beginning
a
