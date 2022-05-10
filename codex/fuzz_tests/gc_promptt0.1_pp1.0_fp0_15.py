import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print "callback", wr

def test():
    f = Foo()
    wr = weakref.ref(f, callback)
    print "created", wr
    del f
    print "deleted"
    gc.collect()
    print "collected"

test()

# Test gc.garbage

class Foo:
    pass

def test():
    f = Foo()
    wr = weakref.ref(f)
    print "created", wr
    del f
    print "deleted"
    gc.collect()
    print "collected"
    print "garbage:", gc.garbage

test()

# Test gc.get_referrers()

class Foo:
    pass

def test():
    f = Foo()
    wr = weakref.ref(f)
    print "created", wr
    del f
    print "deleted"
    gc.collect()
    print "collected"
    print "garbage:", g
