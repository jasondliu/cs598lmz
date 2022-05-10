import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b

f()
gc.collect()

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
    return gc.collect()

f()

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
    return gc.collect(2)

f()

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
