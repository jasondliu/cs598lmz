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

# Simple encoding tests
def test_simple_encode():
    assert 'abc'.encode('ascii') == b'abc'
    assert '\xe9'.encode('ascii', 'strict') == b'\xc3\xa9'
    assert '\xe9'.encode('ascii', 'ignore') == b''
    assert '\xe9'.encode('ascii', 'replace') == b'?e'
    assert '\xe9'.encode('ascii', 'xmlcharrefreplace') == b'&#233;'
    assert '\xe9'.encode('ascii', 'backslashreplace') == b'\\xe9'
    assert '\xe9'.encode('ascii', 'namereplace') == b'\\N{LATIN SMALL LETTER E WITH ACUTE}'
    assert '\xe9'.encode('ascii', 'add_one_codepoint') == b'ae'
    raises(UnicodeEncodeError, '\xe9'.encode, 'ascii', '
