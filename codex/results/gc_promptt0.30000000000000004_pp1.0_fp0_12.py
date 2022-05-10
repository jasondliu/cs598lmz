import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def f():
    f1 = Foo()
    f2 = Foo()
    f3 = Foo()
    b1 = Bar()
    b2 = Bar()
    b3 = Bar()
    f1.b = b1
    f2.b = b2
    f3.b = b3
    b1.f = f1
    b2.f = f2
    b3.f = f3
    del f1, f2, f3, b1, b2, b3
    gc.collect()

f()

# Test gc.get_objects()

def f():
    f1 = Foo()
    f2 = Foo()
    f3 = Foo()
    b1 = Bar()
    b2 = Bar()
    b3 = Bar()
    f1.b = b1
    f2.b = b2
    f3.b = b3
    b1.f = f1
    b2.f = f2
    b
