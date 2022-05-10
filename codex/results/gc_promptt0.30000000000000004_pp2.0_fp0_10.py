import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()

class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
