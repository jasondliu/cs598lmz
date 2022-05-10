import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
gc.collectable(foo)
gc.collectable(bar)
gc.collectable(foo2)
gc.collectable(bar2)
# Create references to all of the objects
r1 = weakref.ref(foo)
r2 = weakref.ref(bar)
r3 = weakref.ref(foo2)
r4 = weakref.ref(bar2)
# The objects are all still alive
r1() is foo
r2() is bar
r3() is foo2
r4() is bar2
# Delete the objects
del foo
del bar
del foo2
del bar2
gc.collect()
# The objects are all dead
r1() is None
r2() is None
r3() is None
r4() is None
del r1, r2, r3, r4
gc.collect()

# Test weakref.WeakKeyDictionary
# Create some weakly-referencable objects
class Foo(object): pass
class Bar(object): pass
foo = Foo()
bar = Bar()
foo2 = Foo()
bar2 =
