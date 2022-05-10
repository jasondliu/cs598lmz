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

def test_unicode_decode():
    inp = b'\xA1\x96'
    if sys.byteorder == 'little':
        inp = reversed(inp)
    inp = b''.join(inp)

    test_encodings = ['utf-16be', 'utf-16le', 'utf-32be', 'utf-32le']
    for encoding in test_encodings:
        assert str(inp, encoding, 'ignore') == ''
        assert str(inp, encoding, 'replace').encode(encoding) == b'\ufffd'
        assert str(inp, encoding, 'add_one_codepoint') == 'a'
        assert str(inp, encoding, 'add_utf16_bytes') == 'ab'
        assert str(inp, encoding, 'add_utf32_bytes') == 'abcd'

def test_unicode_encode():
    test_strings = ['\uABCD', 'asd\uABCD', '\uABCDasd']
    test_enc
