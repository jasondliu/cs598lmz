import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo:
    def __init__(self, x):
        self.x = x

def foo():
    f = Foo(1)
    r = weakref.ref(f)
    f.x = 2
    del f
    gc.collect()
    assert r() is None

foo()

class Foo:
    def __init__(self, x):
        self.x = x
        self.r = weakref.ref(self)

def foo():
    f = Foo(1)
    f.x = 2
    del f
    gc.collect()

foo()

class Foo:
    def __init__(self, x):
        self.x = x
        self.r = weakref.ref(self)

def foo():
    f = Foo(1)
    f.x = 2
    del f
    gc.collect()

foo()

class Foo:
    def __init__(self, x):
        self.x = x
        self.r = weakref.
