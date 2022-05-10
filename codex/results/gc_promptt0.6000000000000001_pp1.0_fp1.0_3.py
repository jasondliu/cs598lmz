import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A:
    pass
a=A()
a.x=A()
a.x.y=a
a.x.y.z=a.x
del a
gc.collect()
print gc.get_referrers(A)

class B:
    pass
b=B()
b.x=B()
b.x.y=b
b.x.y.z=b.x
del b
gc.collect()
print gc.get_referrers(B)

# Test weakref
class C:
    pass
c=C()
c.x=C()
c.x.y=c
c.x.y.z=c.x
w=weakref.ref(c)
del c
gc.collect()
print w()
print gc.get_referrers(C)
