import codecs
# Test codecs.register_error
def test_register_error():
    class X(Exception):
        pass
    def handler(exc):
        if isinstance(exc, X):
            print "hello world"
            return u"", exc.end
        raise exc

    # Register a local error handler
    codecs.register_error("test.x", handler)
    # Now, calling the error handler should print "hello world"
    # codecs.charmap_decode(s, "strict", "test.x")
    s = b"foobar"
    u = s.decode("ascii", "test.x")
    print u
    # Should raise an exception, because no handler was registered
    # for the "ignore" error
    try:
        s.decode("ascii", "ignore")
    except LookupError:
        pass
    else:
        print "failed"
    # Now, registering the error handler should work
    codecs.register_error("test.ignore", codecs.ignore_errors)
    s.decode("ascii", "test.ignore")
