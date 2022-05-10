import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f

func()

gc.collect()
gc.collect()
gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

class Bar:
    pass

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f

func()

gc.collect()
gc.collect()
gc.collect()

# Test gc.get_referents()

class Foo:
    pass

class Bar:
    pass

def func():
    f = Foo()
    b = Bar()
    f.b = b
    b.f = f

func()

gc.collect()
gc.collect()
gc.collect()

# Test gc.get_objects()

class Foo:
    pass

class Bar:
    pass
