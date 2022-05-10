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
    a = None
    gc.collect()
    print gc.garbage
    del gc.garbage[:]

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

l = [A, B, C, D]
t = (a, b, c, d)
d = {'a':a, 'b':b, 'c':c, 'd':d}

print gc.get_referrers(A)
print gc.get_referrers(B)
print gc.get_referrers(C)
print gc.get_referrers(D)
print gc.get_referrers(a)
print gc.get_referrers(b)
print
