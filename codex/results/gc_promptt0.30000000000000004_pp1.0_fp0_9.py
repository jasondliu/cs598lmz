import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class Foo:
    pass

def callback(obj):
    print "callback"

def main():
    f = Foo()
    w = weakref.ref(f, callback)
    del f
    gc.collect()
    print w() is None

main()
