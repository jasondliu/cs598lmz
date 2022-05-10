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

def testUnicodeObject():

    # Error handling
    assert codecs.decode("abc\x80def", "latin-1", "ignore") == u"abcdef"
    assert codecs.decode("abc\x80def", "latin-1", "replace") == u"abc?def"
    assert codecs.decode("abc\x80def", "latin-1", "backslashreplace") == u"abc\\x80def"

    assert codecs.decode("abc\x80def", "latin-1", "strict")
    raises(UnicodeDecodeError, codecs.decode, "abc\x80def", "latin-1")

    assert codecs.decode("abc\x80def", "latin-1", "add_one_codepoint") == u"abcaef"
    assert codecs.decode("abc\x80def", "latin-1", "add_utf16_bytes") == u"abcaef"

    assert codecs.decode("abc\x80def", "
