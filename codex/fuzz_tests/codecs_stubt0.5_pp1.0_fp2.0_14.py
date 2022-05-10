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

def test_codecs(encoding):
    assert codecs.lookup_error("add_one_codepoint")(
        UnicodeDecodeError(encoding, b'\xff', 0, 1, "ouch")) == ("a", 1)
    assert codecs.lookup_error("add_one_codepoint")(
        UnicodeEncodeError(encoding, "\u1234", 0, 1, "ouch")) == ("a", 1)
    assert codecs.lookup_error("add_utf16_bytes")(
        UnicodeDecodeError(encoding, b'\xff\xff', 0, 2, "ouch")) == (b'ab', 2)
    assert codecs.lookup_error("add_utf16_bytes")(
        UnicodeEncodeError(encoding, "\u1234", 0, 1, "ouch")) == (b'ab', 2)
    assert codecs.lookup_error("add_utf32_bytes")(
        UnicodeDecodeError(encoding, b'\xff\xff\xff\xff', 0, 4, "ouch"))
