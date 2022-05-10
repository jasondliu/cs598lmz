import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print "in bar"
    f = Foo()
    wr = weakref.ref(f, bar)
    print "wr:", wr
    print "f:", f
    print "wr():", wr()
    print "f is wr():", f is wr()
    del f
    print "f is wr():", f is wr()
    print "wr():", wr()
    print "wr:", wr
    print "calling gc.collect()"
    gc.collect()
    print "wr:", wr
    print "wr():", wr()
    print "done"

bar()
