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

def test_utf_16_be():
    assert b'\xff\xfe\x01\x00\x00\x00\x01\x00'.decode('utf-16-be') == '\U00010000'

def test_utf_16_le():
    assert b'\xfe\xff\x00\x01\x00\x00\x00\x01'.decode('utf-16-le') == '\U00010000'

def test_utf_16_ex_le():
    assert b'\xfe\xff\x00\x01\x00\x00\x00\x01'.decode('utf-16-le', 'add_utf16_bytes') == '\U00010000a'

def test_utf_16_ex_be():
    assert b'\xff\xfe\x01\x00\x00\x00\x01\x00'.decode('utf-16-be', 'add_utf16_bytes') == '\U00010000a'

def test_utf_32_
