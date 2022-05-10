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
    # Test various error handlers
    try:
        '\u0100'.encode('ascii')
    except UnicodeEncodeError as exc:
        assert exc.object == '\u0100'
        assert exc.encoding == 'ascii'
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == 'ordinal not in range(128)'
        assert str(exc) == '\'ascii\' codec can\'t encode character \'\\u0100\' in position 0: ordinal not in range(128)'
        assert repr(exc) == "UnicodeEncodeError('ascii', '\\u0100', 0, 1, 'ordinal not in range(128)')"

    try:
        '\u0100'.encode('ascii', 'ignore')
    except UnicodeEncodeError as exc:
        assert exc.object == '\u0100'
        assert exc.encoding == 'ascii'
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason ==
