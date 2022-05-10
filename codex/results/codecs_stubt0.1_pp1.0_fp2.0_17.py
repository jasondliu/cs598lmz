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
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'surrogateescape', 'surrogatepass'):
            for input, expected in [
                (b'\x80', u'\ufffd'),
                (b'\xc0', u'\ufffd'),
                (b'\xc0\x80', u'\ufffd\ufffd'),
                (b'\xc0\xaf', u'\ufffd\ufffd'),
                (b'\xc1\x80', u'\ufffd'),
                (b'\xc1\xbf', u'\ufffd'),
                (b'\xc2\x80', u'\u0080'),
                (b'\xc2\xbf', u'\u00bf'),
                (b'\xc3\x80', u'\u00c0'),
                (b'\xc3\xbf',
