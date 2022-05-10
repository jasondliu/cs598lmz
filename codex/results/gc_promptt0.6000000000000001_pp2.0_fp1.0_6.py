import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs.
w = weakref.ref(42)
gc.collect()
# Test gc.collect() on weakrefs.

class Foo(object):
    pass

class Bar(object):
    pass

x = Foo()
y = Foo()
x.attr = y
y.attr = x
del x, y
gc.collect()
# Test gc.collect() on weakrefs.

class Foo(object):
    pass

class Bar(object):
    pass

x = Foo()
y = Foo()
x.attr = y
y.attr = x
del y
gc.collect()
# Test gc.collect() on weakrefs.

class Foo(object):
    pass

class Bar(object):
    pass

x = Foo()
y = Foo()
x.attr = y
y.attr = x
del x
gc.collect()
# Test gc.collect() on weakrefs.

class Foo(object):
    pass

class Bar(object):
    pass

x = Foo()

