import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def do_test(cache):
    class A:
        pass
    class B:
        pass
    a = A()
    b = B()
    a.b = b
    b.a = a
    cache[1] = a
    cache[2] = b
    del a, b
    gc.collect()
    for k, v in cache.items():
        print(k, ":", v)
    print()

print("Testing cache with weak values:")
cache = weakref.WeakValueDictionary()
do_test(cache)

print("Testing cache with strong values:")
cache = {}
do_test(cache)

# Verify that __del__ is called on objects which are cyclic,
# but have no references to any other objects.
def do_test_del(cache):
    class A:
        def __init__(self):
            self.a = self
        def __del__(self):
            print("del")
            cache[1] = None
        def __repr__(self):
            return "A()
