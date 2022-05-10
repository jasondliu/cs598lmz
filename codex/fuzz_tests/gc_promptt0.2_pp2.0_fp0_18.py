import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    a = Foo()
    a.b = Foo()
    a.b.a = a
    del a
    gc.collect()

bar()

# Test gc.get_referrers()

class Foo(object):
    pass

def bar():
    a = Foo()
    a.b = Foo()
    a.b.a = a
    del a
    gc.collect()

bar()

# Test gc.get_referents()

class Foo(object):
    pass

def bar():
    a = Foo()
    a.b = Foo()
    a.b.a = a
    del a
    gc.collect()

bar()

# Test gc.get_objects()

class Foo(object):
    pass

def bar():
    a = Foo()
    a.b = Foo()
    a.b.a = a
    del a
    gc.collect()

bar()

# Test g
