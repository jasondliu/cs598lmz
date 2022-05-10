import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class C(object):
    pass

class D(object):
    pass

def callback(w):
    print "callback called"

def main():
    c = C()
    d = D()
    c.d = d
    d.c = c
    wr = weakref.ref(c, callback)
    del c, d
    gc.collect()
    print wr()
    gc.collect()
    print wr()

main()
