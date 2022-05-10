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


# Test the basic functionality.
def test_basic():
    assert codecs.encode("foo\xffbar", "utf-8") == b'foo\xffbar'
    assert codecs.decode(b'foo\xffbar', "utf-8") == "foo\ufffdbar"
    assert codecs.encode("foo\uffffbar", "utf-16") == b'\xff\xfe\x00f\x00o\x00o\x00\xff\xfb\x00b\x00a\x00r'
    assert codecs.decode(b'\xff\xfe\x00f\x00o\x00o\x00\xff\xfb\x00b\x00a\x00r', "utf-16") == "foo\uffffbar"
    assert codecs.encode("foo\U0010ffffbar", "utf-32") == b'\xff\xfe\x00\x00\x00f\x00\x00\x00o\x00\x00\x00o\x00
