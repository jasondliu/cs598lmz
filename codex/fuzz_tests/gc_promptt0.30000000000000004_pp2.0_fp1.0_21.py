import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    print "in bar"
    f = Foo()
    wr = weakref.ref(f, bar)
    print "wr:", wr
    print "f:", f
    print "wr():", wr()
    print "f is wr():", f is wr()
    print "wr in gc.garbage:", wr in gc.garbage
    print "f in gc.garbage:", f in gc.garbage
    print "gc.collect()"
    gc.collect()
    print "wr:", wr
    print "f:", f
    print "wr():", wr()
    print "f is wr():", f is wr()
    print "wr in gc.garbage:", wr in gc.garbage
    print "f in gc.garbage:", f in gc.garbage
    print "del f"
    del f
    print "wr:", wr
    print "f:", f
    print "wr():", wr()
    print "f
