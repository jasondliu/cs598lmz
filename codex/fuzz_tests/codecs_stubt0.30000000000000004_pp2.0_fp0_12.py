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
    # Test that the default error handler is "strict"
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        try:
            codecs.decode(b'\xff', encoding)
        except UnicodeDecodeError:
            pass
        else:
            raise TestFailed('expected UnicodeDecodeError')

    # Test the "replace" error handler
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        s = codecs.decode(b'\xff', encoding, 'replace')
        if s != '\ufffd':
            raise TestFailed('"replace" error handler failed')

    # Test the "ignore" error handler
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        s = codecs.decode(b'\xff', encoding, 'ignore')
        if s != '':
            raise TestFailed('"ignore" error handler failed')

    # Test the "xmlcharrefreplace" error handler
    for encoding in ('
