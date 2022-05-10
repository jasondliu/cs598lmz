import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref
class Foo(object):
    def __del__(self):
        print "deleted"

class Bar(object):
    def __init__(self, foo):
        self.foo = foo

foo = Foo()
bar = Bar(foo)

foo_ref = weakref.ref(foo)
assert foo_ref() is foo

del foo
gc.collect()
assert foo_ref() is None

del bar
gc.collect()

# Test weakref with __del__
class Foo2(object):
    def __init__(self, bar):
        self.bar = bar
    def __del__(self):
        print "deleted"

class Bar2(object):
    def __init__(self, foo):
        self.foo = foo

foo = Foo2(None)
bar = Bar2(foo)
foo.bar = bar

foo_ref = weakref.ref(foo)
assert foo_ref() is foo

del foo
gc.collect()
assert foo_ref()
