import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def f():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b

f()
gc.collect()

# Test gc.get_objects()

class Foo:
    pass

class Bar:
    pass

def f():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b

f()
gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

class Bar:
    pass

def f():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b

f()
gc.collect()

# Test gc.get_referents()

class Foo:
    pass

class Bar:
    pass

def f():
    a = Foo()
    b =
