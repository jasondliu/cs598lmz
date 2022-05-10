import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# We create a bunch of objects that are collectable and check that
# gc.collect() collects them.  We also check that gc.collect() doesn't
# collect objects that are not collectable.

# Create a bunch of collectable objects
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Create a bunch of uncollectable objects
class E:
    def __del__(self):
        pass

class F(E):
    pass

class G(E):
    pass

class H(F, G):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
g = G()
h = H()

# Check that gc.collect() collects all the collectable objects
gc.collect()
assert a in gc.garbage
assert b in gc.garbage
assert c in gc.garbage
assert d in gc.gar
