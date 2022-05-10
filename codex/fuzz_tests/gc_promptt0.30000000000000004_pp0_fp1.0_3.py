import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(object):
    pass

gc.collect()

a = A()
b = B()
c = C()
d = D()
e = E()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc.collect()
print gc.collect()

print gc
