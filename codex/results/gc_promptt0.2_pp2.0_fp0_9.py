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
x_id = id(x)
del x
gc.collect()
assert w() is None
assert gc.collect() == 0

x = B()
y = C()
w = weakref.ref(x)
x_id = id(x)
del x
gc.collect()
assert w() is None
assert gc.collect() == 0

x = B()
y = C()
w = weakref.ref(y)
y_id = id(y)
del y
gc.collect()
assert w() is None
assert gc.collect() == 0

x = B()
y = C()
w = weakref.ref(x)
x_id = id(x)
del x
gc.collect()
assert w() is None
assert gc.collect() == 0

x = B()

