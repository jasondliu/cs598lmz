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
    # Test encoding
    for encoding in ['utf-8', 'utf-16', 'utf-32']:
        for error_handler in [None, 'strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']:
            if error_handler == 'add_utf16_bytes' and encoding != 'utf-16':
                continue
            if error_handler == 'add_utf32_bytes' and encoding != 'utf-32':
                continue
            try:
                codecs.encode(b'\x80', encoding, error_handler)
            except UnicodeEncodeError:
                pass
            else:
                raise AssertionError("UnicodeEncodeError not raised")

    # Test decoding
    for encoding in ['utf-8', 'utf-16', 'utf-32']:
        for error_handler in [None, 'strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32
