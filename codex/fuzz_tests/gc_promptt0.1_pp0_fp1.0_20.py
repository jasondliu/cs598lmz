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

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

l = [A(), B(), C(), D()]
t = (A(), B(), C(), D())
d = {'a':A(), 'b':B(), 'c':C(), 'd':D()}

def f():
    return A()

r = f()

# Test gc.get_referents()

gc.get_referents(a)
gc.get_referents(b)
gc.get_referents(c)
gc.get_referents(d)
gc.get_referents(l)
gc.get_referents(t)

