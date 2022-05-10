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
    print "before", gc.collect()
    del f
    print "after", gc.collect()

test()

# Test gc.garbage

class Foo:
    pass

def test():
    f = Foo()
    wr = weakref.ref(f)
    print "created", wr
    print "before", gc.collect()
    del f
    print "after", gc.collect()
    print "garbage", gc.garbage

test()

# Test gc.get_referrers()

class Foo:
    pass

def test():
    f = Foo()
    wr = weakref.ref(f)
    print "created", wr
    print "before", gc.collect()
    del f
    print "after", gc.collect()
    print "garbage",
