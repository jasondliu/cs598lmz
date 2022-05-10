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

def main():
    exc = UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
    u = exc.object + "def"
    assert u == '\xffdef'
    u = exc.object + "abc"
    assert u == '\xffabc'
    u = exc.object + "ab"
    assert u == '\xffab'
    u = exc.object + "a"
    assert u == '\xffa'

    exc = UnicodeEncodeError("ascii", '\ud800', 0, 1, "ouch")
    b = exc.object.encode("ascii", "add_one_codepoint")
    assert b == b'\xffa'
    b = exc.object.encode("utf-16", "add_one_codepoint")
    assert b == b'\xff\x00a\x00'
    b = exc.object.encode("utf-32", "add_one_codepoint")
    assert b == b'\xff\x00\x00\
