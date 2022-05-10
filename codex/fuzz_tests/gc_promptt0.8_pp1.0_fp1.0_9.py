import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() is not necessary.

class Foo:
    pass

def callback(obj):
    print('Callback on', repr(obj))

k = Foo()
wr = weakref.ref(k, callback)
del k
print(gc.collect())
print(wr())
print(callback.__self__)
print(wr.__self__)
print(gc.collect())
