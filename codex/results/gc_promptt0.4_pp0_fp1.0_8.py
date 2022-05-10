import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def func():
    f = Foo()
    g = Foo()
    f.f = f
    f.g = g
    g.f = f
    g.g = g
    return f

def func2():
    f = Foo()
    g = Foo()
    f.f = f
    f.g = g
    g.f = f
    g.g = g
    return g

def func3():
    f = Foo()
    g = Foo()
    f.f = f
    f.g = g
    g.f = f
    g.g = g
    return f, g

def func4():
    f = Foo()
    g = Foo()
    f.f = f
    f.g = g
    g.f = f
    g.g = g
    return g, f

def func5():
    f = Foo()
    g = Foo()
    f.f = f
    f.g = g
    g.f = f
   
