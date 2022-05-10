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

def test_unicode_decode_error():
    # Test UnicodeDecodeError
    for encoding in ['ascii', 'utf-8', 'utf-16', 'utf-32']:
        try:
            u"\xff".encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == "\xff"
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "ordinal not in range(128)"
            assert str(exc) == " 'ascii' codec can't encode character '\\xff' in position 0: ordinal not in range(128)"
        else:
            assert False, "Did not raise UnicodeEncodeError"
        try:
            u"\xff".encode(encoding, "replace")
        except UnicodeEncodeError as exc:
            assert exc.object == "\xff"
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "ordinal not in
