fn = lambda: None
# Test fn.__code__
test_fn.__code__ = CodeType(0, 0, 0, 0, b'', (None,), (), (), '', '', 0, b'')

def test_module():
    """Validate that modules are serialized correctly"""
    cPickle = cPickle as cPickle
    # This test should serialize successfully
    for proto in protocols:
        s = cPickle.dumps(sys, proto)
        newmod = cPickle.loads(s)
        # newmod.argv won't exist on Windows, but we don't want to test
        # that here.  So delete sys.argv before the test, then restore
        # it after.
        try:
            argv = sys.argv
            del sys.argv
            assert_equal(newmod.__name__, 'sys')
            assert_equal(newmod.__dict__, sys.__dict__)
        finally:
            sys.argv = argv
    # This should fail because the code pickling process isn't
    # complete yet.
    assert_raises(
