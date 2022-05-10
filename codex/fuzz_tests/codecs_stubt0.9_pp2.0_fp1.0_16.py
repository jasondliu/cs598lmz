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

def test_utf16be_errors(testf):
    testf.write_testfile('utf16be')
    f = TextIOWrapper(testf.open('utf16be'), encoding='utf-16-be')
    f.read()
    f.seek(0)
    f.write(u'abc\ud800\udfff')
    f.flush()
    f.seek(0)
    eq = assert_equal
    s = u'abc\ud800\udfff'
    eq(s, f.read())
    eq(s, f.read())

    # Surrogates in non-BMP plane
    f = TextIOWrapper(testf.open('utf16be'), encoding='utf-16-be',
                      errors='add_one_codepoint')
    eq(s, f.read())

    f = TextIOWrapper(testf.open('utf16be'), encoding='utf-16-be',
                      errors='surrogateescape')
    # On reading the character \ud800 the UTF-16 decoder raises an
