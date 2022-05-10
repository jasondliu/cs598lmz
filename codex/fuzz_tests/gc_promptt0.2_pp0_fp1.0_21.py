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
    gc.collect()
    print(gc.collect())

test()

# Test gc.get_referrers()

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
    gc.collect()
    print(gc.get_referrers(Foo))
    print(gc.get_referrers(Bar))

test()

# Test gc.get_referents()

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
    gc.collect()
    print
