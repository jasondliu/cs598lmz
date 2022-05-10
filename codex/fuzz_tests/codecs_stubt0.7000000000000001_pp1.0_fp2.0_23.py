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
    encoding = "utf-32"
    try:
        codecs.lookup(encoding)
    except LookupError:
        pytest.skip("%s is not supported" % encoding)

    # The default encoding error handler should add one codepoint
    u = u'\ufffd'
    x = u.encode(encoding, "add_one_codepoint")
    assert len(x) == 4
    d = x.decode(encoding)
    assert len(d) == 1
    assert d == u'a'

    # The default decoding error handler should add one codepoint
    x = b'\x00\x00\x00\x00'
    u = x.decode(encoding, "add_one_codepoint")
    assert len(u) == 1
    d = u.encode(encoding)
    assert len(d) == 4
    assert d == b'\x00\x00\x00\x00'

    # The default encoding error handler should add one codep
