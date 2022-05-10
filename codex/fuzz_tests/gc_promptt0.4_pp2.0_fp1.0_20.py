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
class E(D):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()

# Create a cycle involving the new classes
d.a = a
a.b = b
b.c = c
c.d = d

# Break the cycle
a.b = None
b.c = None
c.d = None
del a, b, c, d

# Collecting E should also collect the rest
gc.collect()

# Check that E is gone
try:
    e.a
except AttributeError:
    pass
else:
    print "e.a was not collected"

# Check that the rest are gone
for obj in [a, b, c, d]:
    try:
        obj.a
    except NameError:
        pass
    else:
        print "%s was not collected" % obj

# Check that we can
