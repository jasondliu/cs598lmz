import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    pass

def f():
    a = Foo()
    b = Foo()
    a.b = b
    b.a = a
    del a
    del b
    gc.collect()

f()
gc.garbage

# Test gc.collect() with a cyclic garbage with __del__
# and a __del__ that resurrects an object.
class Foo(object):
    def __del__(self):
        self.b = Foo()

def f():
    a = Foo()
    a.b = Foo()
    a.b.b = a
    del a
    gc.collect()

f()
gc.garbage

# Test gc.collect() with a cyclic garbage with __del__
# and a __del__ that resurrects an object.
# The object is not in the cyclic garbage.
class Foo(object):
    def __del__(self):
        self.b = Foo()

def f():
    a = Foo()
    a.b = Foo()
    a
