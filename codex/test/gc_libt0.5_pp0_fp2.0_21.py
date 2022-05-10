import gc, weakref

def test_gc():
    class A(object):
        pass
    class B(object):
        pass
    a = A()
    a.b = B()
    a.b.a = a
    weakref_a = weakref.ref(a)
    del a
    gc.collect()
    assert weakref_a() is None

def test_gc_2():
    class A(object):
        pass
    a = A()
    weakref_a = weakref.ref(a)
    del a
    gc.collect()
    assert weakref_a() is None

def test_gc_3():
    class A(object):
        pass
    class B(object):
        pass
    a = A()
    a.b = B()
    a.b.a = a
    weakref_a = weakref.ref(a)
    del a
    gc.collect()
    assert weakref_a() is None

def test_gc_4():
    class A(object):
        pass
