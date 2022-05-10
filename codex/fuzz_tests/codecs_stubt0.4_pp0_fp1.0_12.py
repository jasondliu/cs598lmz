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

def test_utf8_error(encoding):
    assert codecs.decode(b'\x80', encoding, 'add_one_codepoint') == '\u0080'
    assert codecs.decode(b'\x80', encoding, 'add_utf16_bytes') == '\u0080a'
    assert codecs.decode(b'\x80', encoding, 'add_utf32_bytes') == '\u0080ab'

def test_utf16_error(encoding):
    assert codecs.decode(b'\x80\x00', encoding, 'add_one_codepoint') == '\u0080'
    assert codecs.decode(b'\x80\x00', encoding, 'add_utf16_bytes') == '\u0080a'
    assert codecs.decode(b'\x80\x00', encoding, 'add_utf32_bytes') == '\u0080ab'

def test_utf32_error(encoding):
    assert codecs.decode(
