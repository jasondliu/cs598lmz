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

def test_codecs():

    # UTF-8
    #
    # ADD_ONE_CODEPOINT
    #
    # b'\x80' <-> U+000080 (second byte encoding)
    #
    assert codecs.decode(b'\x80', 'utf-8', errors='add_one_codepoint') == '\x80a'
    assert codecs.encode('\x80', 'utf-8', errors='add_one_codepoint') == b'\x80a'
    #
    # b'\xC0\x80' <-> U+000080 (first byte encoding)
    #
    assert codecs.decode(b'\xC0\x80', 'utf-8', errors='add_one_codepoint') == 'a'
    assert codecs.encode('a', 'utf-8', errors='add_one_codepoint') == b'\xC0\x80a'
    #
    # b'\xC0' <-> U+000080 (
