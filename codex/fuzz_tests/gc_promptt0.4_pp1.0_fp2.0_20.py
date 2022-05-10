import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    def __init__(self):
        self.foo = Foo()

b = Bar()

print gc.collect()

del b

print gc.collect()

# Test gc.get_objects()

class Foo:
    pass

class Bar:
    def __init__(self):
        self.foo = Foo()

b = Bar()

print gc.get_objects()

del b

print gc.get_objects()

# Test gc.get_referrers()

class Foo:
    pass

class Bar:
    def __init__(self):
        self.foo = Foo()

b = Bar()

print gc.get_referrers(Foo)

del b

print gc.get_referrers(Foo)

# Test gc.get_referents()

class Foo:
    pass

class Bar:
    def __init__(self):
        self.foo = Foo()

