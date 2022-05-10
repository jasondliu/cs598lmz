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
    test_unicode_internal_encode()
    test_unicode_internal_decode()

def test_unicode_internal_encode():
    # test internal Unicode encoding
    assert '\u3042'.encode('utf-8') == b'\xe3\x81\x82'
    assert '\u3042'.encode('utf-16') == b'\xff\xfeB\x00'
    assert '\u3042'.encode('utf-32') == b'\xff\xfe\x00\x00B\x00\x00\x00'
    assert '\u3042'.encode('raw_unicode_escape') == b'\\u3042'
    assert '\u3042'.encode('unicode_escape') == b'\\u3042'
    assert '\u3042'.encode('unicode_internal') == b'\x42\x30'

    # test decoding to Unicode
    assert b'\xe3\x81\x82'.decode('utf
