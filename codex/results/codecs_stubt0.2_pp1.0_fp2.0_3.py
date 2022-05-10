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
    # Test UTF-8
    for encoding in ('utf-8', 'utf_8'):
        # Test decoding
        for input, expected in [
            (b'\xc2\x80', '\u0080'),
            (b'\xc2\xbf', '\u00bf'),
            (b'\xc3\x80', '\u00c0'),
            (b'\xc3\xbf', '\u00ff'),
            (b'\xc4\x80', '\u0100'),
            (b'\xc4\xbf', '\u017f'),
            (b'\xc5\x80', '\u0180'),
            (b'\xc5\xbf', '\u024f'),
            (b'\xc6\x80', '\u0250'),
            (b'\xc6\xbf', '\u02af'),
            (b'\xc7\x80', '\u02b0'),
            (b'\xc7\xbf', '
