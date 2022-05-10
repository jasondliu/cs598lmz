import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A(object):
    pass

class B(object):
    pass

a = A()
b = B()

wr = weakref.ref(a)

print wr()

del a

gc.collect()

print wr()

print gc.collect()
