import weakref
# Test weakref.ref()
def test_weakref_keyerror():
    t = weakref.WeakValueDictionary()
    try:
        raise KeyError
    except KeyError:
        exc = sys.exc_info()[1]
        t.__getitem__(exc) # make sure an entry for the current exception exists
        r = weakref.ref(exc)
        assert r() is exc
        r = None
        assert not t
    assert not t
    try:
        raise KeyError
    except KeyError:
        exc = sys.exc_info()[1]
        assert t[exc] is exc
        r = weakref.ref(exc)
        assert r() is exc
        r = None

    assert not t
    try:
        raise KeyError
    except KeyError:
        pass
    assert not t
    try:
        raise KeyError
    except KeyError:
        exc = sys.exc_info()[1]
        assert t[exc] is exc
        r = weakref.ref(exc)
        assert r() is exc
        del t[exc]
