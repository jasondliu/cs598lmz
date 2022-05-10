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

def test_u1():
    """ test UTF-8 with add_one_codepoint error handler """
    text = '\xc3\x28'
    u = text.decode("utf-8", "add_one_codepoint")
    utf8 = u.encode("utf-8")
    assert utf8 == '\xc3\x61\xc3\x28'

def test_u2():
    """ test UTF-16 with add_utf16_bytes error handler """
    text = b'abcd'
    u = text.decode("utf-16", "add_utf16_bytes")
    utf16 = u.encode("utf-16")
    assert utf16 == b'ab\xff\xfea\x00b\x00'

def test_u3():
    """ test UTF-32 with add_utf32_bytes error handler """
    text = b'abcdefgh'
    u = text.decode("utf-32", "add_utf32_bytes")
    utf32 = u.en
