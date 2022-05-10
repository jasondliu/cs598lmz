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

def test_utf8_decode(encoding):
    # Issue #1393: UTF-8 decoding failed if the last character was
    # an invalid continuation byte.
    for i in range(0x80, 0x100):
        s = bytes([0xf5, i])
        try:
            s.decode(encoding)
        except UnicodeDecodeError as e:
            assert e.object[e.start] == i
            assert e.end == e.start + 1
            assert e.reason == "unexpected end of data"
        else:
            assert False, "expected decode error"
        s = bytes([0xf5, i, 0xa0])
        try:
            s.decode(encoding)
        except UnicodeDecodeError as e:
            assert e.object[e.start] == i
            assert e.end == e.start + 1
            assert e.reason == "unexpected end of data"
        else:
            assert False, "expected decode error"
    # Issue #1393: UTF-8 decoding failed if the last character was
