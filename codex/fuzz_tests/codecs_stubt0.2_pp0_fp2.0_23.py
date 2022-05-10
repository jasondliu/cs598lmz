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

def test_main():
    # Test UTF-8
    assert codecs.utf_8_decode(b'\x80') == ('\uFFFD', 1)
    assert codecs.utf_8_decode(b'\x80', 'replace') == ('\ufffd', 1)
    assert codecs.utf_8_decode(b'\x80', 'ignore') == ('', 1)
    assert codecs.utf_8_decode(b'\x80', 'add_one_codepoint') == ('a', 1)
    assert codecs.utf_8_decode(b'\x80', 'add_utf16_bytes') == ('ab', 1)
    assert codecs.utf_8_decode(b'\x80', 'add_utf32_bytes') == ('abcd', 1)
    assert codecs.utf_8_decode(b'\x80', 'strict') == ('', 1)
    assert codecs.utf_8_decode(b'\x80', 'surrogateescape') == ('
