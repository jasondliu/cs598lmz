import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def f():
    a = Foo('a')
    b = Foo('b')
    c = Foo('c')
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    del a, b, c
    gc.collect()
    print gc.collect()
    print gc.garbage

f()

# Test gc.get_objects()

def f():
    a = Foo('a')
    b = Foo('b')
    c = Foo('c')
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    del a, b, c
    gc.collect()
    print gc.collect()
    print gc.get_objects()

f()

# Test gc.get_re
