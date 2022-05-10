import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def f():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f

f()
gc.collect()

# Test gc.get_objects()

def f():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f()
gc.collect()

# Test gc.get_referrers()

def f():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f()
gc.collect()

# Test gc.get_referents()

def f():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f

f()
gc.collect()

# Test gc.get_threshold()

# Test gc.set_threshold()

# Test g
