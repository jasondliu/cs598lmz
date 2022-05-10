import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, name):
        self.name = name

def f():
    a = Foo("a")
    b = Foo("b")
    a.b = b
    b.a = a
    return a

a = f()

# Check that a is collectable
assert gc.is_tracked(a)
assert gc.is_tracked(a.__dict__)
assert gc.is_tracked(a.b)
assert gc.is_tracked(a.b.__dict__)
assert gc.is_tracked(a.b.a)
assert gc.is_tracked(a.b.a.__dict__)

# Check that a is not collectable
gc.collect()
assert not gc.is_tracked(a)
assert not gc.is_tracked(a.__dict__)
assert not gc.is_tracked(a.b)
assert not gc.is_tracked(a.b.__dict__)
