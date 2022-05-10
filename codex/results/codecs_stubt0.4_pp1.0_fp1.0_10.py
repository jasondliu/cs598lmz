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

def check_error_callback(encoding, input, expected):
    try:
        codecs.decode(input, encoding, "add_one_codepoint")
    except UnicodeDecodeError as exc:
        assert exc.object == input
        assert exc.start == len(input)
        assert exc.end == len(input)
        assert exc.reason == 'invalid continuation byte'
        assert exc.encoding == encoding
        assert exc.object[exc.start:exc.end] == b''
        assert str(exc) == expected
    else:
        assert False

def test_utf8():
    check_error_callback("utf-8", b'\xff', "invalid continuation byte at position 0")
    check_error_callback("utf-8", b'\xff\xff', "invalid continuation byte at position 0")
    check_error_callback("utf-8", b'\xff\xff\xff', "invalid continuation byte at position 0")
    check_error_callback("utf-8", b'\xff\xff\xff\xff', "in
