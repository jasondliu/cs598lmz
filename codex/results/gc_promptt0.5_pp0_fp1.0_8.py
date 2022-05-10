import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def test_gc_collect():
    class A:
        pass
    a = A()
    assert gc.collect() == 0
    del a
    assert gc.collect() == 1

# Test gc.collect() with a gc.garbage cycle
def test_gc_collect_garbage():
    class A:
        pass
    a = A()
    a.a = a
    assert gc.collect() == 0
    del a
    assert gc.collect() == 1

# Test gc.collect() with a gc.garbage cycle containing a __del__ method
def test_gc_collect_garbage_del():
    class A:
        def __del__(self):
            pass
    a = A()
    a.a = a
    assert gc.collect() == 0
    del a
    assert gc.collect() == 1

# Test gc.collect() with a gc.garbage cycle containing a __del__ method
# that raises an exception
def test_gc_collect_garbage_del_exception():
