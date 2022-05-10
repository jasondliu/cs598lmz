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
        for error_handler in ('strict', 'ignore', 'replace', 'add_one_codepoint'):
            for input, expected in (
                (b'\x80', '\ufffd'),
                (b'\xc0\x80', '\ufffd\ufffd'),
                (b'\xc0\xc0', '\ufffd\ufffd'),
                (b'\xc0', '\ufffd'),
                (b'\xc1', '\ufffd'),
                (b'\xc0\xaf', '\ufffd\ufffd'),
                (b'\xe0\x80\x80', '\ufffd\ufffd\ufffd'),
                (b'\xe0\x80', '\ufffd\ufffd'),
                (b'\xe0\x80\xaf', '\ufffd\ufffd\ufffd'),
                (b'\xe0\x81\x81', '
