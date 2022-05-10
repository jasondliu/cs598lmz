import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
#b = A()
#a.b = b
#b.a = a
#del a, b
#print(gc.collect())

# Test gc.get_objects()

a = A()
l = gc.get_objects()
print(len(l), l[:10])
del a
print(len(l), l[:10])
