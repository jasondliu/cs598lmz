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
    # Test UTF-16 and UTF-32 codecs
    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be',
                     'utf-32', 'utf-32-le', 'utf-32-be'):
        # Test decoding
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            for input, expected in (
                # Test decoding of BOM
                (b'\xff\xfe', '\ufeff'),
                (b'\xfe\xff', '\ufeff'),
                (b'\xff\xfe\x00\x00', '\ufeff'),
                (b'\x00\x00\xfe\xff', '\ufeff'),
                # Test decoding of non-BOM
                (b'\x00\x00', '\x00\x00'),
                (b'\x00\x00\x00\x00', '
