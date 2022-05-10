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

def test_utf8(encoding):
    # Test UTF-8 decoding
    assert codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', "strict", True) == (
        '\U0010ffff', 4)
    assert codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', "strict", False) == (
        '\U0010ffff', 4)
    assert codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', "replace", True) == (
        '\ufffd\ufffd\ufffd\ufffd', 4)
    assert codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', "replace", False) == (
        '\ufffd\ufffd\ufffd\ufffd', 4)
    assert codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', "ignore", True)
