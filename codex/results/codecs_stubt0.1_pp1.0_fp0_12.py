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
    assert codecs.utf_8_decode(b'\xff')[0] == '\ufffd'
    assert codecs.utf_8_decode(b'\xff', 'replace')[0] == '\ufffd'
    assert codecs.utf_8_decode(b'\xff', 'ignore')[0] == ''
    assert codecs.utf_8_decode(b'\xff', 'add_one_codepoint')[0] == 'a'
    assert codecs.utf_8_decode(b'\xff', 'add_utf16_bytes')[0] == 'ab'
    assert codecs.utf_8_decode(b'\xff', 'add_utf32_bytes')[0] == 'abcd'

    # Test UTF-16
    assert codecs.utf_16_decode(b'\xff')[0] == '\ufffd'
    assert codecs.utf_16_decode(b'\xff', 'replace')[0
