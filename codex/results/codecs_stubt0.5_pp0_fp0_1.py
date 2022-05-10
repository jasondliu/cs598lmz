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
    # Test UTF-16-LE codec
    assert codecs.utf_16_le_decode(b'abcd', "strict") == ('abcd', 4)
    assert codecs.utf_16_le_decode(b'abcd', "replace", "add_one_codepoint") == ('ab\ufffd', 4)
    assert codecs.utf_16_le_decode(b'abcd', "replace", "add_utf16_bytes") == ('ab\ufffd', 4)
    assert codecs.utf_16_le_decode(b'abcd', "replace", "add_utf32_bytes") == ('ab\ufffd', 4)
    assert codecs.utf_16_le_decode(b'ab', "strict") == ('', 2)
    assert codecs.utf_16_le_decode(b'ab', "replace", "add_one_codepoint") == ('a', 2)
    assert codecs.utf_16_le_decode(b'ab', "replace
