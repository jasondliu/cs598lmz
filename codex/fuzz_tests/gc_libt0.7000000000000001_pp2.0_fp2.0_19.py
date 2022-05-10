import gc, weakref
import weakref as pytest
import numpy as np

def test_weak_ref():
    class Foo:
        pass
    f = Foo()
    f.a = 1
    a = weakref.WeakKeyDictionary()
    a[f] = 1
    assert f.a == 1
    del f
    gc.collect()
    assert len(a) == 0

def test_weak_value():
    class Foo:
        pass
    f = Foo()
    f.a = 1
    a = weakref.WeakValueDictionary()
    a[1] = f
    assert f.a == 1
    del f
    gc.collect()
    assert len(a) == 0

def test_get_weakref():
    class A:
        pass
    a = A()
    ar = weakref.ref(a)
    assert ar() is a

def test_weak_key_in_list():
    class Foo:
        pass
    f = Foo()
    f.a = 1
    a = weakref.WeakKeyD
