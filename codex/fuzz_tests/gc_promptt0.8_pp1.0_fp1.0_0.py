import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after weakref.proxy is destroyed

class Foo:
    def __del__(self):
        pass

f = Foo()

f.x = Foo()
f.y = weakref.proxy(f.x)
f.x.z = weakref.ref(f.x)

f.x = None
f.y = None

gc.collect()

assert gc.collect() == 0
print('passed all tests')
