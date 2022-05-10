import weakref
# Test weakref.ref_create()

def wr(x):
    return weakref.ref(x)

def test_basic():
    class C:
        pass
    o = C()
    r = wr(o)
    assert r() is o

def test_callable():
    class C:
        def __call__(self):
            return 42
    o = C()
    r = wr(o)
    assert r() is o
    assert r()() == 42

def test_del():
    class C:
        pass
    o = C()
    r = wr(o)
    assert r() is o
    del o
    assert r() is None

def test_del_during_callback():
    l = []
    class C:
        pass
    def callback(wr):
        l.append(wr())
        del o
    o = C()
    r = wr(o, callback)
    del o
    assert l == [None]
    assert r() is None

def test_callback_during_callback():
    l = []
    class
