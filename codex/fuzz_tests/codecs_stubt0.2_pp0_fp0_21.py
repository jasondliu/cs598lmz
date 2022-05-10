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

def test_utf8_decode():
    # Test UTF-8 decoding
    assert '\u3042'.encode('utf-8').decode('utf-8') == '\u3042'
    assert '\u3042'.encode('utf-8').decode('utf-8', 'strict') == '\u3042'
    assert '\u3042'.encode('utf-8').decode('utf-8', 'ignore') == ''
    assert '\u3042'.encode('utf-8').decode('utf-8', 'replace') == '\ufffd'
    assert '\u3042'.encode('utf-8').decode('utf-8', 'add_one_codepoint') == 'a\u3042'
    assert '\u3042'.encode('utf-8').decode('utf-8', 'add_utf16_bytes') == '\u3042\u3042'
    assert '\u3042'.encode('utf-8').decode('utf-8', 'add_utf32_bytes
