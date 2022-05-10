import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Foo %s>' % self.name

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
    gc.collect()
    print gc.garbage

f()

# Test gc.get_referrers()

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
    gc.collect()
    print gc.get_referrers(Foo)

f()

# Test gc.get_referents()

def f():
    a = Foo('a')
    b = Foo('b')
    a.b = b
    b.a = a
    del a
    del b
    gc
