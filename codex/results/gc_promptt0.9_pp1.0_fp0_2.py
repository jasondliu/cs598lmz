import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.collect(2)

class A:
    pass
a = A()
a.x = A()
a.y = A()
a.x.a = a
a.x.y = a.y
del a
gc.collect(2)
print('OK')
