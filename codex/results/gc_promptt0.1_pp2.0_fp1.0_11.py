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
    b1 = Bar()
    b2 = Bar()
    f1.b = b1
    f2.b = b2
    b1.f = f1
    b2.f = f2
    del f1, f2, b1, b2
    gc.collect()

f()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect
