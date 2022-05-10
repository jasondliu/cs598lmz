import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(x):
    print("callback", x)

def test():
    f = Foo()
    r = weakref.ref(f, callback)
    print("callback", r())
    del f
    print("collecting")
    gc.collect()
    print("callback", r())

test()
