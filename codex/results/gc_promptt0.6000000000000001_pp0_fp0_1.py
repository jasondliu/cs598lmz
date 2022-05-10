import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weak reference to a function.
def get_func():
    def f():
        pass

    return f

def test_collect():
    f = get_func()
    wr = weakref.ref(f)
    del f
    gc.collect()
    assert wr() is None

# Test gc.collect with a weak reference to a module.
def test_collect_module():
    import sys
    wr = weakref.ref(sys)
    del sys
    gc.collect()
    assert wr() is None

def test_collect_module2():
    import sys
    wr = weakref.ref(sys)
    del sys
    gc.collect()
    assert wr() is None

# Test gc.collect with a weak reference to a class.
def test_collect_class():
    class A:
        pass

    A() # create a reference to A
    wr = weakref.ref(A)
    del A
    gc.collect()
    assert wr() is None

def test_collect_class2():
    class A
