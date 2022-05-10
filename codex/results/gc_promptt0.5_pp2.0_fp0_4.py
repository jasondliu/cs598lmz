import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when there are uncollectable objects.
class A:
    pass

class B(A):
    pass

a = A()
b = B()
b.foo = a
a.foo = b
del a, b
gc.collect()
# Test gc.collect() when there are uncollectable objects.
class A:
    pass

class B(A):
    pass

a = A()
b = B()
b.foo = a
a.foo = b
del a, b
gc.collect()
# Test gc.collect() when there are uncollectable objects.
class A:
    pass

class B(A):
    pass

a = A()
b = B()
b.foo = a
a.foo = b
del a, b
gc.collect()
# Test gc.collect() when there are uncollectable objects.
class A:
    pass

class B(A):
    pass

a = A()
b = B()
b.foo = a
a.foo = b
del a, b
gc.
