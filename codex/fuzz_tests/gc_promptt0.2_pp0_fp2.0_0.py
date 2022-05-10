import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def f():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a

def g():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b

def h():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b
    gc.collect()

def i():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b
    gc.collect()
    gc.collect()

def j():
    a = Foo()
    b = Bar()
    a.b = b
    b.a = a
    del a, b
    gc.collect()
    gc.collect()
    gc.collect()

def k():
    a = Foo()
   
