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

# Test UTF-8

def test_utf8(input, errors):
    dec = codecs.getdecoder("utf-8")
    enc = codecs.getencoder("utf-8")
    if errors is None:
        errors = "strict"
    for s, exp_decoded in input:
        res = dec(s, errors)
        assert res == exp_decoded
        res = enc(exp_decoded, errors)
        assert res == (s, len(s))

def test_utf8_errors():
    test_utf8([("\xff", ("\ufffd", 1))], "replace")
    test_utf8([("\xff", ("\ufffd", 1))], "ignore")
    test_utf8([("\xff", ("\ufffd", 1))], "surrogateescape")
    test_utf8([("\xff", ("\ufffd", 1))], "surrogatepass")
    test_utf8([("\xff", ("\ufffd", 1))], "xmlcharrefreplace")
    test_utf8
