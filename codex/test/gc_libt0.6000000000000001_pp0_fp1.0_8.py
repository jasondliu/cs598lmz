import gc, weakref

def test_weakref_with_del():
    l = []
    for i in range(10):
        obj = object()
        l.append(weakref.ref(obj, lambda x: l.remove(x)))
    assert len(l) == 10
    del obj
    gc.collect()
    assert len(l) == 0


def test_weakref_list_with_del():
    l = []
    for i in range(10):
        obj = object()
        l.append(weakref.ref(obj, l.remove))
    assert len(l) == 10
    del obj
    gc.collect()
    assert len(l) == 0


class A(object):
    pass

def test_weakref_list_with_del_2():
    a = A()
    l = []
    l.append(weakref.ref(a, l.remove))
    assert len(l) == 1
    del a
    gc.collect()
    assert len(l) == 0


