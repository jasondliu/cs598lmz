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

# UTF-8
def test_utf8_decode(encoding):
    # make sure illegal utf-8 characters are handled
    for c in [b'\x80', b'\x80'*2, b'\x80'*3, b'\x80'*4]:
        # test decoding with errors='strict'
        assert_raises(UnicodeDecodeError, encoding.decode, c)
        # test decoding with errors='replace'
        assert_equal(encoding.decode(c, 'replace'), '\ufffd')
        # test decoding with errors='ignore'
        assert_equal(encoding.decode(c, 'ignore'), '')
        # test decoding with errors=<function>
        assert_equal(encoding.decode(c, add_one_codepoint), 'a')
        # test decoding with errors=<exception subclass>
        assert_raises(LookupError,
                      encoding.decode, c, LookupError)
        # if the error callback returns a unicode string, it must be able to
