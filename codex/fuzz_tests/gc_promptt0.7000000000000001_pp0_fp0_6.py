import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class A:
    pass

refs = []

for i in range(10):
    a = A()
    refs.append(weakref.ref(a))
    del a

gc.collect()

print len(gc.garbage), gc.collect()

for ref in refs:
    assert ref() is None
