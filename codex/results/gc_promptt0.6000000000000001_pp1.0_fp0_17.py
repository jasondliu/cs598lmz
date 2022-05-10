import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after __del__()

class Foo:
    def __del__(self):
        pass

f = Foo()
f.__del__()
f = None
gc.collect()

# Test gc.collect() after __del__()

class Foo:
    def __del__(self):
        pass

f = Foo()
f.__del__()
f.__del__()
gc.collect()

# Test gc.collect() after __del__()

class Foo:
    def __del__(self):
        pass

f = Foo()
f.__del__()
f.__del__()
f = None
gc.collect()

# Test gc.collect() after __del__()

class Foo:
    def __del__(self):
        pass

f = Foo()
f.__del__()
f = None
f = None
gc.collect()

# Test gc.collect() after __del__()

class Foo:
    def __del__(self):
        pass

f = Foo()
