import weakref
# Test weakref.ref(x) and weakref.proxy(x)

class C:
    pass

def test_weakref_ref():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    c = None
    #assert r() is None

def test_weakref_proxy():
    c = C()
    p = weakref.proxy(c)
    assert p is c
    c = None
    raises(ReferenceError, "p.foo")

# Test weakref.ref(x, callback)

class R:
    def __init__(self, callback):
        self.callback = callback
        self.called = False
    def __call__(self):
        self.called = True
        self.callback()

def test_weakref_ref_callback():
    l = []
    def func():
        l.append(1)
    c = R(func)
    r = weakref.ref(c, func)
    assert r() is c
    c = None
    assert l == [1]
    assert
