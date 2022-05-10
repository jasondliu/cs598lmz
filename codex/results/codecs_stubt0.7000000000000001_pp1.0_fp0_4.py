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

def c_encode_errorhandler_callbacks(encoding):
    """
    This tests the error handler callback mechanism in the C codecs
    """
    test_string = 'abc'
    # test 1: add one codepoint
    codecs.register_error("test1", add_one_codepoint)
    result = test_string.encode(encoding, errors="test1")
    assert result == b'aabc'
    # test 2: add some UTF-16 bytes
    if encoding == "utf-16":
        codecs.register_error("test2", add_one_codepoint)
    else:
        codecs.register_error("test2", add_utf16_bytes)
    result = test_string.encode(encoding, errors="test2")
    if encoding == "utf-16":
        assert result == b'a\0a\0b\0c'
    else:
        assert result == b'a\0\0\0\0b\0\0\0\0c'
    # test 3:
