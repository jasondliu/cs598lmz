import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    pass

a = Foo()
b = Foo()
a.x = b
b.x = a
del a
del b
gc.collect()

# Test gc.get_referents()
class Foo(object):
    pass

a = Foo()
b = Foo()
a.x = b
b.x = a
del a
del b
gc.collect()

class Foo(object):
    pass

a = Foo()
b = Foo()
a.x = b
b.x = a
del a
del b
gc.collect()

class Foo(object):
    pass

a = Foo()
b = Foo()
a.x = b
b.x = a
del a
del b
gc.collect()

class Foo(object):
    pass

a = Foo()
b = Foo()
a.x = b
b.x = a
del a
del b
gc.collect()

class Foo(object):
    pass

a = Foo()
b = Foo()
a
