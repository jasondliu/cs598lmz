import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Start by creating a bunch of objects
class Foo(object):
    pass

class Bar(object):
    pass

class Baz(object):
    pass

class Qux(object):
    pass

foo = Foo()
bar = Bar()
baz = Baz()
qux = Qux()

print gc.collect()

# Now, make them weakly reachable
def func():
    pass

foo.func = func
func.foo = foo
foo.bar = bar
bar.baz = baz
baz.qux = qux
qux.foo = foo

print gc.collect()

# Now, make them unreachable
foo = None
bar = None
baz = None
qux = None

print gc.collect()
