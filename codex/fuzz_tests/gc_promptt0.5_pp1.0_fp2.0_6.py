import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, name):
        self.name = name

def f():
    a = Foo('a')
    b = Foo('b')
    wr = weakref.ref(a)
    print wr
    del a
    print wr
    # force collection of a
    gc.collect()
    print wr

f()

# Test gc.get_referrers()

def f():
    a = Foo('a')
    b = Foo('b')
    wr = weakref.ref(a)
    print wr
    del a
    print wr
    print gc.get_referrers(wr)

f()

# Test gc.get_referents()

def f():
    a = Foo('a')
    b = Foo('b')
    wr = weakref.ref(a)
    print wr
    del a
    print wr
    print gc.get_referents(wr)

f()

# Test gc.get_objects()


