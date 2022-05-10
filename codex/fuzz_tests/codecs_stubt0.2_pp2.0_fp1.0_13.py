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

# Test encoding

def test_encode(encoding, input, errors, expected):
    assert codecs.encode(input, encoding, errors) == expected

def test_encode_error(encoding, input, errors, expected):
    try:
        codecs.encode(input, encoding, errors)
    except UnicodeEncodeError as exc:
        assert exc.object == input
        assert exc.encoding == encoding
        assert exc.start == expected.start
        assert exc.end == expected.end
        assert exc.reason == expected.reason
        assert exc.object[exc.start:exc.end] == expected.object
    else:
        assert False, "Did not raise"

def test_encode_error_callback(encoding, input, errors, expected):
    assert codecs.encode(input, encoding, errors) == expected

def test_encode_error_callback_exc(encoding, input, errors, expected):
    try:
        codecs.encode(input, encoding, errors)
    except UnicodeEncodeError as exc:
