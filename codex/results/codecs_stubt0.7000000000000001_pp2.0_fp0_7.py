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

def test_unicode_encode_errors(test_string, encoding):
    u = unicode(test_string, encoding)
    s = codecs.escape_decode(u.encode("unicode-escape"))[0]
    assert s == test_string, "Encoding failed"
    def do_test(errors):
        u.encode(encoding, errors=errors)
    yield do_test, "strict"
    yield do_test, "replace"
    yield do_test, "xmlcharrefreplace"
    yield do_test, "backslashreplace"
    yield do_test, "ignore"
    yield do_test, "add_one_codepoint"
    if encoding == "utf-16-le":
        yield do_test, "add_utf16_bytes"
    if encoding == "utf-32-le":
        yield do_test, "add_utf32_bytes"

def test_unicode_decode_errors(test_string):
    u = unicode(test_string, "unicode-escape")
