import weakref
# Test weakref.ref(obj)

def test():
    class C:
        pass

    c = C()
    r = weakref.ref(c)
    assert r() is c
    del c
    assert r() is None


def test_weakref_callback():
    class C:
        pass

    def callback(r):
        assert r() is c
        l.append(1)

    c = C()
    l = []
    r = weakref.ref(c, callback)
    assert r() is c
    del c
    import gc
    gc.collect()
    assert r() is None
    assert l == [1]
    l = []
    c = C()
    r = weakref.ref(c, callback)
    assert r() is c
    del r
    import gc
    gc.collect()
    assert l == [1]
    assert c.__weakref__() is None


def test_weakref_callback_exc():
    class C:
        pass

    def callback(r):
        raise ValueError

    c
