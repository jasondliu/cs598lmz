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

for c in [A, B, C, D]:
    a = c()
    a.foo = a
    del a
    gc.collect()
    print len(gc.garbage)

a = A()
a.foo = a
gc.collect()
print len(gc.garbage)
del a
gc.collect()
print len(gc.garbage)

# Test gc.get_referrers()

class C:
    pass

gc.collect()
print len(gc.garbage)

a = A()
a.foo = a
b = B()
b.foo = b
c = C()
c.foo = c

print len(gc.get_referrers(a))
print len(gc.get_referrers(b))
print len(gc.get_referrers(c))

print len(gc.get_re
