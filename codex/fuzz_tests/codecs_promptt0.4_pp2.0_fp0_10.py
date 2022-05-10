import codecs
# Test codecs.register_error()

def test_register_error():
    # Test that codecs.register_error() works.
    # (This test is a bit lame, but it's better than nothing.)
    #
    # The idea is to register an error handler that raises an exception,
    # then try to encode a Unicode string with a character that can't be
    # encoded.  The exception will be caught by the encoder and the
    # resulting UnicodeEncodeError will be passed to the error handler.
    # The error handler will re-raise the exception.
    #
    # If the error handler is not called, the test will fail.

    # The exception to raise
    class Error(Exception):
        pass

    # The error handler
    def handler(exception):
        raise Error(exception)

    # Register the error handler
    codecs.register_error("test.error", handler)

    # Try to encode a Unicode string with a character that can't be encoded
    try:
        u"\u1234".encode("ascii", "test.error")
    except Error:
        pass

