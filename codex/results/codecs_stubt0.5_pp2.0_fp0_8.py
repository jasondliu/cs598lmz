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

def test_decode():
    # test decode with byteorder argument
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'ignore') == (b'd', 2)
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'replace') == (b'?d', 2)
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'backslashreplace') == (b'\\ufffbd', 2)
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'xmlcharrefreplace') == (b'&#65533;d', 2)
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'namereplace') == (b'\\ufffbd', 2)
    assert codecs.utf_16_decode(b'\xff\xfeb\x00d', 'add_one_codepoint') == ('ad', 2)

