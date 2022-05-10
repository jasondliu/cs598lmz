import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

class C(object):
    pass

c = C()
d = C()
c.d = d
d.c = c

class D(object):
    pass

e = D()
f = D()
e.f = weakref.ref(f)
f.e = weakref.ref(e)
del f, e
gc.collect()

# Test gc.collect() with uncollectable objects
class G:
    pass

g = G()
h = G()
g.h = h
h.g = g

class I(object):
    pass

i = I()
j = I()
i.j = j
j.i = i

class J(object):
    pass

k = J()
l = J()
k.l = weakref.ref(l)
l.k = weakref.ref(k)
del l, k
gc.collect()
gc.collect
