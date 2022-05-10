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

def test_utf8_error_handling():
    # Issue #15710: UTF-8 should not silently ignore invalid bytes
    for error_handler in (None, 'strict', 'replace', 'ignore',
                          'add_one_codepoint'):
        for bad_byte in (b'\xff', b'\xfe', b'\x00'):
            if error_handler == 'add_one_codepoint':
                # When 'add_one_codepoint' is specified, the bad byte is
                # replaced by a single codepoint.
                decoded = '\ufffd'
            elif error_handler == 'replace':
                # When 'replace' is specified, the bad byte is replaced
                # by the Unicode replacement character.
                decoded = '\ufffd'
            elif error_handler == 'ignore':
                # When 'ignore' is specified, the bad byte is silently
                # ignored.
                decoded = ''
            elif error_handler is None:
                # When no error handler is specified, the default error
                # handler
