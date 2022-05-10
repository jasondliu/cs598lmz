import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class MyClass(object):
    pass

gc.collect()

class MyClass2(object):
    pass

gc.collect()

w = weakref.ref(MyClass())
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

gc.collect
