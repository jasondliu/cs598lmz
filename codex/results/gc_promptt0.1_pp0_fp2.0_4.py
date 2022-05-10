import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def callback(wr):
    print "callback", wr

def test():
    f = Foo()
    wr = weakref.ref(f, callback)
    print "created", wr
    del f
    gc.collect()
    print "collected"

test()

# Test gc.get_referrers()

class Foo(object):
    pass

def test():
    f = Foo()
    r = gc.get_referrers(f)
    print r

test()

# Test gc.get_referents()

class Foo(object):
    pass

def test():
    f = Foo()
    r = gc.get_referents(f)
    print r

test()

# Test gc.get_objects()

class Foo(object):
    pass

def test():
    f = Foo()
    r = gc.get_objects()
    print r

test()

# Test gc.is_tracked()
