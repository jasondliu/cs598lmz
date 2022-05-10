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

# Test UnicodeEncodeError

def test_unicodeencode_error():
    # test UnicodeEncodeError
    for encoding in ['ascii', 'utf-8', 'utf-16', 'utf-32']:
        try:
            u'\xff'.encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == u'\xff'
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == 'ordinal not in range(128)'
            assert str(exc) == '\'%s\' codec can\'t encode character \'\\xff\' in position 0: ordinal not in range(128)' % encoding
        else:
            assert False, "didn't raise UnicodeEncodeError"

        try:
            u'\xff'.encode(encoding, 'add_one_codepoint')
        except UnicodeEncodeError as exc:
            assert exc.object == u'\xff'
            assert exc.encoding == encoding
            assert exc.start == 0

