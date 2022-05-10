import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
class A:
    pass
a = A()
a.b = A()
b = a.b
a.b.c = a

a_wr = weakref.ref(a)
del a
count = gc.collect()
print(count)
a = a_wr()
print(a)
a.b = None
count = gc.collect()
print(count)
print(a)
