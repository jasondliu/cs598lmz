import weakref
# Test weakref.ref() and weakref.proxy()
def test_factory(factory, cyclic=True):
    wr = factory(C)
    assert isinstance(wr, (weakref.ref, weakref.ProxyType))
    if cyclic:
        C.wr = wr
    del C
    gc.collect()
    if cyclic:
        assert wr() is None
    else:
        assert wr() is C
    assert isinstance(wr, (weakref.ref, weakref.ProxyType))

def test_factory_failing(factory):
    try:
        wr = factory(C)
        assert False, "didn't raise"
    except TypeError:
        pass

def tests():
    global C
    class C(object):
        pass
    c = C()
    test_factory(weakref.ref)
    test_factory(weakref.ref, False)
    test_factory(weakref.proxy)
    C.__hash__ = lambda self: 42
    test_factory_failing(weakref.ref)
   
