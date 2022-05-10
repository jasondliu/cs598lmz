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

# Issue #10984
# UTF-16-LE codec with surrogatepass error handling
def test_utf16_surrogatepass(encoding):
    utf16 = codecs.getencoder(encoding)
    utf16_dec = codecs.getdecoder(encoding)
    u = '\ud800\udc00'
    s, length = utf16(u, 'surrogatepass')
    assert length == 2
    u2, length2 = utf16_dec(s, 'surrogatepass')
    assert length2 == 2
    assert u == u2

def test_utf16_invalid():
    u = '\ud800\udc00\ud800'
    s, length = codecs.utf_16_encode(u, 'surrogatepass')
    assert length == 3
    u2, length2 = codecs.utf_16_decode(s, 'surrogatepass')
    assert length2 == 3
    assert u == u2

def test_utf32_invalid():
    u =
