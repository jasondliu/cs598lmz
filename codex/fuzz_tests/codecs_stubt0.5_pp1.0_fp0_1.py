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

def test_errorhandler():
    def check(input, encoding, errors, expected):
        actual = codecs.decode(input, encoding, errors)
        assert actual == expected, "%r != %r" % (actual, expected)

    check(b'\xff', "ascii", "add_one_codepoint", "a\uffff")
    check(b'\xff', "ascii", "add_utf16_bytes", "a\uffff")
    check(b'\xff', "ascii", "add_utf32_bytes", "a\uffff")
    check(b'\xff', "utf-16", "add_one_codepoint", "\uffff")
    check(b'\xff', "utf-16", "add_utf16_bytes", "\uffff")
    check(b'\xff', "utf-16", "add_utf32_bytes", "\uffff")
    check(b'\xff', "utf-32", "add_one_codepoint", "\uffff")
    check(b'\xff
