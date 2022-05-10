import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class A(object):
    pass
a = A()
a.b = A()
a.b.a = a
a_wr = weakref.ref(a)
print gc.collectable(a)
print gc.collectable(a.b)
print gc.collectable(a_wr)
del a
print gc.collectable(a_wr)
print gc.collect()
print gc.collectable(a_wr)
print gc.collect()
print gc.collectable(a_wr)

# Test gc.get_referrers()
class A(object):
    pass
a = A()
b = A()
a.b = b
b.a = a
c = []
c.append(b)
d = {}
d[1] = a
print gc.get_referrers(a)
print gc.get_referrers(b)
print gc.get_referrers(c)
print gc.get_referrers(d)

# Test gc.
