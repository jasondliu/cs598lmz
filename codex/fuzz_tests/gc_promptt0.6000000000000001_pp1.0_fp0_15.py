import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that is called when the
# weakrefable object is collected.

class C:
    pass

def callback(arg):
    print "callback"

def main():
    c = C()
    weakref.ref(c, callback)
    del c
    gc.collect()

main()
