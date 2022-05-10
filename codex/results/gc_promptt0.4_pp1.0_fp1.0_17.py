import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class X(object):
    pass

class Y(object):
    pass

class Z(object):
    pass

x = X()
y1 = Y()
y2 = Y()
z = Z()

x.y = y1
y1.x = x
y1.z = z
y2.z = z

del x, y1, y2, z

gc.collect()

# Test gc.get_referrers() and gc.get_referents()

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

a = A()
b = B()
c = C()

a.b = b
b.a = a
b.c = c
c.b = b

del a, b, c

gc.collect()

# Test gc.get_objects()

class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

d = D
