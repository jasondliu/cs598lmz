import codecs
# Test codecs.register_error

def test_register_error():
    # Test the register_error() function
    # This is a bit tricky, because we need to check that the
    # error handler is actually called.  We do this by raising
    # an exception in the error handler.  The exception should
    # propagate out of the codec.decode() call.

    # The error handler we'll register
    def raise_exception(exception):
        raise exception

    # Register the error handler
    codecs.register_error("test.raising_exception", raise_exception)

    # Now try to use the error handler
    try:
        codecs.decode("foo", "ascii", "test.raising_exception")
    except UnicodeDecodeError:
        pass
    else:
        raise TestFailed("error handler didn't get called")

    # Now try to use the error handler with a different exception
    try:
        codecs.decode("foo", "ascii", "test.raising_exception(LookupError)")
    except LookupError:
        pass
    else
