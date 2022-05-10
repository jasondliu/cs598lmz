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

def test_unicode_error_message():
    # Test that UnicodeDecodeError and UnicodeEncodeError have a
    # human-readable error message
    for codec in ['ascii', 'utf-7', 'utf-8', 'utf-16', 'utf-32']:
        for obj, offset in [('abc\xff', 3),
                            (b'abc\xff', 3),
                            ('abc\ufffe', 3),
                            (b'abc\xfe\xff', 3),
                            ('abc\U0010ffff', 3)]:
            try:
                obj.encode(codec)
            except UnicodeEncodeError as exc:
                assert exc.object == obj
                assert exc.start == offset
                assert str(exc)
            try:
                obj.decode(codec)
            except UnicodeDecodeError as exc:
                assert exc.object == obj
                assert exc.start == offset
                assert str(exc)

def test_unicode_error_message_surrogatepass():
    # Test that UnicodeDecodeError and Unicode
