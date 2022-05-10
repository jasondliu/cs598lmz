import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    pass

def f():
    x = Foo()
    y = x

f()
gc.collect()

# Test gc.collect() with a weakref
class Foo:
    pass

def f():
    x = Foo()
    y = weakref.ref(x)

f()
gc.collect()

# Test gc.collect() with a weakref and a callback
class Foo:
    pass

def f():
    x = Foo()
    y = weakref.ref(x, lambda x: None)

f()
gc.collect()

# Test gc.collect() with a weakref, a callback, and a finalizer
class Foo:
    pass

def f():
    x = Foo()
    y = weakref.ref(x, lambda x: None)
    z = weakref.finalize(x, lambda x: None)

f()
gc.collect()

# Test gc.collect() with a weakref, a callback, and a finalizer
class Foo:
    pass

def
