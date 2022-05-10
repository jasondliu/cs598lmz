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

def test_utf8_decode(codec_name):
    # utf-8-decode tests
    assert codecs.utf_8_decode(b'\x00') == (u'\x00', 1)
    assert codecs.utf_8_decode(b'\x00', final=True) == (u'\x00', 1)
    assert codecs.utf_8_decode(b'\x00', errors='strict') == (u'\x00', 1)
    assert codecs.utf_8_decode(b'\x00', errors='strict', final=True) == (u'\x00', 1)

    assert codecs.utf_8_decode(b'\x80') == (u'\uFFFD', 1)
    assert codecs.utf_8_decode(b'\x80', final=True) == (u'\uFFFD', 1)
    assert codecs.utf_8_decode(b'\x80', errors='strict') == (u'\u
