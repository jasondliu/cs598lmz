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

def check_error_handler(encoding, error_handler, input, expected):
    # Check that error_handler(exc) returns expected
    # when called on input.
    encoder = codecs.getincrementalencoder(encoding)()
    decoder = codecs.getincrementaldecoder(encoding)(error_handler=error_handler)
    encoded = encoder.encode(input)
    decoded = decoder.decode(encoded)
    assert decoded == expected, (decoded, expected)

def test_error_handlers():
    check_error_handler("utf-8", "add_one_codepoint", "abc", "aabc")
    check_error_handler("utf-16", "add_one_codepoint", "abc", "aabc")
    check_error_handler("utf-32", "add_one_codepoint", "abc", "aabc")
    check_error_handler("utf-16-le", "add_utf16_bytes", "abc", "aabc")
    check_error_handler
