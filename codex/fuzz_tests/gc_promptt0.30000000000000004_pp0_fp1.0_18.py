import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()
c = A()

# Create a reference cycle
a.b = b
b.c = c
c.a = a

# Create a reference graph
d = A()
e = A()
f = A()
d.e = e
e.f = f
f.d = d

# Create a reference graph
g = A()
h = A()
i = A()
g.h = h
h.i = i
i.g = g

# Create a reference graph
j = A()
k = A()
l = A()
j.k = k
k.l = l
l.j = j

# Create a reference graph
m = A()
n = A()
o = A()
m.n = n
n.o = o
o.m = m

# Create a reference graph
p = A()
q = A()
r = A()
p.q = q
q.r = r
r.p = p

# Create a
