import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a finalizer
class Foo:
    def __del__(self):
        pass

foo = Foo()
foo.ref = weakref.ref(foo)
foo.bar = 2
del foo
gc.collect()

# Test gc.collect() with a finalizer that resurrects a cyclic trash can
class Foo:
    def __del__(self):
        pass

foo = Foo()
foo.ref = weakref.ref(foo)
foo.bar = 2
import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)
foo = None
gc.collect()

# Test gc.collect() with a finalizer that resurrects an object
class Foo:
    def __del__(self):
        pass

foo = Foo()
foo.ref = weakref.ref(foo)
foo.bar = 2
import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)
foo = None
gc.collect()

# Test gc.collect() with a finalizer that resurrects a cyclic trash can
class Foo:
   
