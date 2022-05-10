import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
# that triggers a gc.collect()

class A:
    pass

class B:
    pass

def callback(wr):
    gc.collect()

def main():
    a = A()
    b = B()
    a.b = b
    b.a = a
    wr = weakref.ref(a, callback)
    del a
    gc.collect()
    print wr()
    del b
    gc.collect()
    print wr()

main()
