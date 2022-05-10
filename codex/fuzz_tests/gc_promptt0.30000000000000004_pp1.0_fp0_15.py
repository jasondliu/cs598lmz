import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

def callback(wr):
    print "callback", wr

class A:
    pass

def main():
    a = A()
    wr = weakref.ref(a, callback)
    print "before", wr
    del a
    gc.collect()
    print "after", wr

main()
