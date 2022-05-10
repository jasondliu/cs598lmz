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
    # Test UnicodeDecodeError handling
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            for start in range(4):
                for end in range(start, 4):
                    try:
                        codecs.decode(b'\xff' * 4, encoding, errors=errors)
                    except UnicodeDecodeError as exc:
                        assert exc.encoding == encoding
                        assert exc.object == b'\xff' * 4
                        assert exc.start == start
                        assert exc.end == end
                        assert exc.reason == 'invalid start byte'
                        assert exc.args == (encoding, b'\xff' * 4, start, end,
                                            'invalid start byte')
                    else:
                        assert errors == 'ignore'

    # Test UnicodeTranslateError handling
    for encoding in ('utf
