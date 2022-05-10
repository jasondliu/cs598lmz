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
    # Test decoding with errors
    assert '\u1234'.encode('ascii', 'add_one_codepoint') == b'a\xe1\x88\xb4'
    assert '\u1234'.encode('utf-16', 'add_one_codepoint') == b'a\x00\xe1\x88\xb4'
    assert '\u1234'.encode('utf-32', 'add_one_codepoint') == b'a\x00\x00\x00\xe1\x88\xb4'

    # Test encoding with errors
    assert b'\xe1\x88\xb4'.decode('ascii', 'add_one_codepoint') == 'a\u1234'
    assert b'\x00\xe1\x88\xb4'.decode('utf-16', 'add_one_codepoint') == 'a\u1234'
    assert b'\x00\x00\x00\xe1\x88\xb4'.
