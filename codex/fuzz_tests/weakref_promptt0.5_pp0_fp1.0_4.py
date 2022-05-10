import weakref
# Test weakref.ref(x, callback)

class MyObj:
    def __init__(self, x):
        self.x = x
        self.called = 0
    def callback(self, ref):
        self.called += 1

def test_ref():
    # Test weakref.ref(object, callback)
    obj = MyObj(10)
    r = weakref.ref(obj, obj.callback)
    assert r() is obj
    assert obj.called == 0
    del obj
    gc.collect()
    assert r() is None
    assert obj.called == 1

def test_proxy():
    # Test weakref.proxy(object, callback)
    obj = MyObj(10)
    p = weakref.proxy(obj, obj.callback)
    assert p.x == 10
    assert obj.called == 0
    del obj
    gc.collect()
    try:
        p.x
    except ReferenceError:
        pass
    else:
        assert False, 'weakref.proxy should have raised ReferenceError'
    assert obj.called == 1

