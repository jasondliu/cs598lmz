import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    del f, b
    gc.collect()

test()

# Test gc.get_referrers()

class Foo(object):
    pass

class Bar(object):
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    del f, b
    gc.collect()

test()

# Test gc.get_referents()

class Foo(object):
    pass

class Bar(object):
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    del f, b
    gc.collect()

test()

# Test gc.get_objects()

class Foo(object):
    pass

class
