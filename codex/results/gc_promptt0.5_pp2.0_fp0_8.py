import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class A:
    pass

a = A()
del a
gc.collect()
print gc.collectable()

# Test gc.get_referrers()
class B:
    pass

b = B()
del b
gc.collect()
print gc.get_referrers(A)

# Test gc.get_referents()
class C:
    pass

c = C()
d = C()
e = C()
c.d = d
c.e = e
del d, e
gc.collect()
print gc.get_referents(c)

# Test gc.get_objects()
class D:
    pass

d = D()
del d
gc.collect()
print gc.get_objects()

# Test gc.get_stats()
class E:
    pass

e = E()
del e
gc.collect()
print gc.get_stats()

# Test gc.garbage
class F:
    def __del__(self):
       
