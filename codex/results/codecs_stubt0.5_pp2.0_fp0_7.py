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

def test_utf8_decode():
    assert '\u1234'.encode('utf-8', 'surrogatepass') == b'\xe1\x88\xb4'
    assert '\ud800'.encode('utf-8', 'surrogatepass') == b'\xed\xa0\x80'
    assert '\udfff'.encode('utf-8', 'surrogatepass') == b'\xed\xbf\xbf'
    assert '\ud800\udc00'.encode('utf-8', 'surrogatepass') == b'\xf0\x90\x80\x80'
    assert '\udbff\udfff'.encode('utf-8', 'surrogatepass') == b'\xf4\x8f\xbf\xbf'
    assert b'\xf0\x90\x80'.decode('utf-8', 'surrogatepass') == '\ud800'
    assert b'\xf0\x90\x80\x80'.decode('utf-8
