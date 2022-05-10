import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class MyClass(object):
    pass

def f():
    x = MyClass()
    x.a = x
    x.b = MyClass()
    x.c = x.b
    x.b.a = x.b
    del x
    #print gc.collect()

f()
gc.collect()
