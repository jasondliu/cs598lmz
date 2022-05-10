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

# UTF-7

def test_utf7_decode_ascii():
    assert codecs.utf_7_decode(b'A+ImIDkQ-') == ('A\x00\x01\x02\x03\x04\x05', 9)

def test_utf7_decode_lone_shift():
    assert codecs.utf_7_decode(b'+', 'replace', True) == ('\ufffd', 1)

def test_utf7_decode_bad_base64():
    assert codecs.utf_7_decode(b'+A+', 'replace', True) == ('\ufffd\x01', 3)

def test_utf7_encode_ascii():
    assert codecs.utf_7_encode('A\x00\x01\x02\x03\x04\x05') == (b'A+ImIDkQ-', 7)

def test_utf7_encode_non_ascii():
    assert codecs.utf_7_en
