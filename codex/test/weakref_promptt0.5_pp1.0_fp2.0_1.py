import weakref
# Test weakref.ref(x)

def test_weakref_ref():
    class C:
        pass
    c = C()
    r = weakref.ref(c)
    assert r() is c
    del c
    assert r() is None

def test_weakref_callback():
    import gc
    L = []
    class C:
        def __init__(self, arg):
            self.arg = arg
        def __del__(self):
            L.append(self.arg)
    c = C(12)
    r = weakref.ref(c, lambda x: x.arg)
    del c
    gc.collect()
    assert L == [12]

def test_weakref_callback_exception():
    import gc
    L = []
    class C:
        def __init__(self, arg):
            self.arg = arg
        def __del__(self):
            L.append(self.arg)
    c = C(12)
    def mycallb(x):
        raise ValueError
    r = weak
