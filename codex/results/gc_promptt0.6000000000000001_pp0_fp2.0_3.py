import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class MyClass:
    pass

def f():
    x = MyClass()
    y = weakref.ref(x)
    gc.collect()
    assert y() is x

f()
# Test gc.collect()
class MyClass:
    pass

def f():
    x = MyClass()
    y = weakref.ref(x)
    gc.collect()
    assert y() is x

f()
# Test gc.collect()
class MyClass:
    pass

def f():
    x = MyClass()
    y = weakref.ref(x)
    gc.collect()
    assert y() is x

f()
# Test gc.collect()
class MyClass:
    pass

def f():
    x = MyClass()
    y = weakref.ref(x)
    gc.collect()
    assert y() is x

f()
# Test gc.collect()
class MyClass:
    pass

def f():
    x = MyClass()
    y = weakref
