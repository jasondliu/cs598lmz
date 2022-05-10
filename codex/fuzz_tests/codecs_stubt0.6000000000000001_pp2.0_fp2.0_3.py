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

def test_utf8_decode_errors():
    # bad utf-8 byte sequence
    s = b'\x80'
    for errors in ('strict', 'ignore', 'replace', 'surrogateescape',
                   'xmlcharrefreplace', 'backslashreplace', 'namereplace',
                   add_one_codepoint, add_utf16_bytes, add_utf32_bytes):
        with pytest.raises((UnicodeDecodeError, TypeError)):
            s.decode('utf-8', errors)

    # bad utf-8 byte sequence
    s = b'\xff'
    for errors in ('strict', 'ignore', 'replace'):
        with pytest.raises(UnicodeDecodeError):
            s.decode('utf-8', errors)

    assert s.decode('utf-8', 'surrogateescape') == '\udcff'
    assert s.decode('utf-8', 'xmlcharrefreplace') == '&#255;'
    assert s.decode('utf-8',
