import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect flag
gc.collect()
gc.get_count()
gc.collect()
gc.get_count()

# Test weakref
class Foo: pass
foo = Foo()
foo.a = Foo()
foo.a.b = foo
foo.a.c = foo.a
foo.a.d = [foo, foo.a]
foo.a.e = weakref.ref(foo.a)
foo.a.f = weakref.ref(foo)
foo.a.g = weakref.ref(foo.a)
del foo
gc.collect()
gc.get_count()
del foo
gc.collect()
gc.get_count()
