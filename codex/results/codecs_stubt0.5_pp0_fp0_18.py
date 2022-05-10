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

def test_decode_error_handling():
    # Test for SF bug #589563 (http://bugs.python.org/issue589563)
    # Check that we don't get a SystemError when decoding a string
    # with an invalid utf-8 byte sequence.
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            try:
                str(b'\xff', encoding, error_handler)
            except UnicodeDecodeError:
                pass

def test_decode_error_handling_ascii():
    # Test for SF bug #589563 (http://bugs.python.org/issue589563)
    # Check that we don't get a SystemError when decoding a string
    # with an invalid utf-8 byte sequence.
    for encoding in ('ascii', 'latin-1'):
        for error_handler
