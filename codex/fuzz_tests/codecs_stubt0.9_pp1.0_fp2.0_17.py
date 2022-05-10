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

def verify_cdata(test_string, test_cdata, test_length=None,
                 ignore_null=True, test_encoding='utf-32'):
    """Test that the test_cdata buffer contains the specifed
    test string and is terminated by a null byte."""
    if isinstance(test_string, str):
        test_string = test_string.encode(test_encoding)

    if test_length is None:
        test_length = len(test_string) + 1
    if ignore_null:
        tail = b'\0'
    else:
        tail = b''
    expected = test_string + tail
    verify(len(test_cdata) >= len(expected),
           "expected cdata of at least length %d, got length %d" %
           (len(expected), len(test_cdata)))
    verify(test_cdata[:len(expected)] == expected,
           "expected cdata '%s', got '%s'" %
           (expected, test_cdata))
    if test_
