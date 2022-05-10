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

x = A()
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None

x = B()
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None

x = C()
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None

x = D()
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None

# Test gc.get_referrers()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = A()
w = weakref.ref(x)
x = None
gc.collect()
assert w() is None

x = B()
