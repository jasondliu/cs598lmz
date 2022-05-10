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
    # Test surrogatepass
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'surrogatepass', 'replace', 'ignore'):
            for text in ('\udc00', '\ud800\udc00', '\ud800\udc00\udc00'):
                try:
                    text.encode(encoding, error_handler)
                except UnicodeEncodeError:
                    pass
                else:
                    raise AssertionError("UnicodeEncodeError not raised")

    # Test backslashreplace
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'surrogatepass', 'replace', 'ignore'):
            for text in ('\udc00', '\ud800\udc00', '\ud800\udc00\udc00'):
                try:
                    text.encode(encoding, error_handler)
                except UnicodeEncodeError:
