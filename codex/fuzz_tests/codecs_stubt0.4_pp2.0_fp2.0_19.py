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

def test_utf8(s, error_handler):
    u = s.decode("utf-8", errors=error_handler)
    s2 = u.encode("utf-8")
    assert s2 == s

def test_utf16(s, error_handler):
    u = s.decode("utf-16", errors=error_handler)
    s2 = u.encode("utf-16")
    assert s2 == s

def test_utf32(s, error_handler):
    u = s.decode("utf-32", errors=error_handler)
    s2 = u.encode("utf-32")
    assert s2 == s

def test_utf7(s, error_handler):
    u = s.decode("utf-7", errors=error_handler)
    s2 = u.encode("utf-7")
    assert s2 == s

def test_utf8_surrogates(error_handler):
    try:
        s = b'\xed\xa0\x80\xed\
