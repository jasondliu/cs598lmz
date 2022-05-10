import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A, B):
    pass

class E(C, D):
    pass

class F:
    pass

class G(F):
    pass

class H(F):
    pass

class I(G, H):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
g = G()
h = H()
i = I()

# Create a reference cycle
a.x = a
b.x = b
c.x = c
d.x = d
e.x = e
f.x = f
g.x = g
h.x = h
i.x = i

# Create a reference graph
a.y = b
b.y = c
c.y = d
d.y = e
e.y = f
f.y = g
g.y = h
h.y = i
i
