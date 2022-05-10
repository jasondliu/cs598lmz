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

def test_utf16_endian_error(encoding):
    try:
        b'\xff\xfea\x00b\x00c\x00\x00\x00'.decode(encoding)
    except UnicodeDecodeError as e:
        assert e.encoding == encoding
        assert e.object == b'\xff\xfea\x00b\x00c\x00\x00\x00'
        assert e.start == 4
        assert e.end == 6
        assert e.reason == 'illegal code bytes'
        assert e.encode(encoding) == b'ab\x00\x00\x00'

def test_utf16le_utf32be_illegal_byte(encoding):
    try:
        b'ab\xff\x00\x00'.decode(encoding)
    except UnicodeDecodeError as e:
        assert e.encoding == encoding
        assert e.object == b'ab\xff\x00\x00'
        assert e.start == 2
        assert e.end
