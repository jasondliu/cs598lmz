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

class X(unicode): pass

def check(encoding, text, handler, expected):
    enc = codecs.getencoder(encoding)
    dec = codecs.getdecoder(encoding)

    try:
        x = enc(text, None)
    except UnicodeEncodeError, e:
        x = enc(text, handler)
    x1 = dec(x, None)[0]
    x2 = dec(x, handler)[0]
    assert x1 == expected
    assert x2 == expected

def test_specific_errors():
    # First we test error handlers that work on the specific exceptions
    # raised by the UTF-* codecs

    # UTF-7
    check("utf-7", u"a+-\u1234", "add_one_codepoint", u"a+-\u1234a")
    check("utf-7", u"a+-\u1234", "add_utf16_bytes", u"a+-\u1234ab")
    check("utf-7", u"a+-\u
