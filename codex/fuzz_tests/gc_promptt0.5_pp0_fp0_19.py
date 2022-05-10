import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() as a generator.
def run_generator_tests():
    # Test gc.collect() as a generator.
    def g():
        yield 1
        yield 2
    x = g()
    x.next()
    x.next()
    del x
    gc.collect()
    def f():
        raise StopIteration
    x = g()
    x.next()
    x.next()
    del x
    gc.collect()
    # Test gc.collect() as a generator.
    def g():
        yield 1
        yield 2
    x = g()
    x.next()
    x.next()
    del x
    gc.collect()
    def f():
        raise StopIteration
    x = g()
    x.next()
    x.next()
    del x
    gc.collect()
    # Test gc.collect() as a generator.
    def g():
        yield 1
        yield 2
    x = g()
    x.next()
    x.next()
    del x
    g
