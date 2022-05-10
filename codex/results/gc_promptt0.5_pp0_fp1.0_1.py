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

a = A()
b = B()
c = C()
d = D()

# create a reference cycle
L = [a, b, c, d]
L.append(L)

# destroy the cycle
del L

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)
c_wr = weakref.ref(c)
d_wr = weakref.ref(d)

# manually run a full collection
gc.collect()

# a_wr and b_wr are still alive because their objects are part of a cycle,
# but c_wr and d_wr are dead because their objects are not part of a cycle
print a_wr(), b_wr(), c_wr(), d_wr()

# manually break the cycle
del a, b, c, d

# a_wr and b_wr are dead because their objects are no longer part
