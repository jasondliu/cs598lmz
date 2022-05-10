import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect

class Foo:
    pass

def f():
    x = Foo()
    x.a = Foo()
    x.b = Foo()
    return x
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


