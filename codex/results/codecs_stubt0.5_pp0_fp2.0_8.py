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

def do_decode(input, errors):
    return codecs.decode(input, "utf-8", errors)

def do_encode(input, errors):
    return codecs.encode(input, "utf-8", errors)

def test_decode():
    assert do_decode(b'\xff', "strict") == (b'\xff', 1)
    assert do_decode(b'\xff', "replace") == (b'?', 1)
    assert do_decode(b'\xff', "ignore") == (b'', 1)
    assert do_decode(b'\xff', "backslashreplace") == (br'\xff', 1)
    assert do_decode(b'\xff', "xmlcharrefreplace") == (b'&#255;', 1)
    assert do_decode(b'\xff', "namereplace") == (b'&ff;', 1)
    assert do_decode(b'\xff\x00', "add_one_codepoint") == ('a\x
