import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    del f, b

test()
gc.collect()
gc.collect()
gc.collect()

# Test gc.garbage

class Foo:
    pass

class Bar:
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f, b

f, b = test()
del f, b
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_objects()

class Foo:
    pass

class Bar:
    pass

def test():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f
    return f, b

f, b = test()
del f, b
gc.collect()
gc.collect()
gc.collect()
