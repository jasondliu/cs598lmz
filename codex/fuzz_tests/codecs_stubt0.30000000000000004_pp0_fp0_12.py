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
    # Test UTF-8
    for errors in ("strict", "ignore", "replace", "add_one_codepoint"):
        for input, output in (
            (b'abc', 'abc'),
            (b'\xff', '\ufffd'),
            (b'\xc0\x80', '\u0000'),
            (b'\xc0\x80\xc0\x80', '\u0000\u0000'),
            (b'\xc0\x80\xc0\x80\xc0\x80', '\u0000\u0000\u0000'),
            (b'\xc0\x80\xc0\x80\xc0\x80\xc0\x80', '\u0000\u0000\u0000\u0000'),
            (b'\xc0\x80\xc0\x80\xc0\x80\xc0\x80\xc0\x80', '\u0000\u0000\u0000\u0000\u0000'),
            (b'\xc0\x
