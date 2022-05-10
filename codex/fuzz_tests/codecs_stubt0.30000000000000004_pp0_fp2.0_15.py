import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_main():
    # Test the codec error handlers
    #
    #     codecs.register_error(errors, handler)
    #
    # where errors is either the name of an error handling
    # scheme or a sequence of names, and handler is a callable
    # that takes an exception instance as argument and returns
    # a (replacement, new position) tuple.
    #
    # The following test is based on the test_codecs.py test
    # written by Marc-Andre Lemburg.

    # Test the error handler API
    try:
        codecs.register_error("test.error", None)
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")

    # Test the error handler API
    try:
        codecs.register_error("test.error", "foo")
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")

    # Test the error handler API
    try:
        codecs.register_error("test.error", lambda x: x)
