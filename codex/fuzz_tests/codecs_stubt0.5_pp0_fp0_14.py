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
    import sys
    if sys.maxunicode == 0xffff:
        utf16_bytes = b'\xff\xfe\x00\x00'
        utf32_bytes = b'\xff\xfe\x00\x00\x00\x00'
    else:
        utf16_bytes = b'\xfe\xff\x00\x00\x00\x00'
        utf32_bytes = b'\x00\x00\xfe\xff\x00\x00\x00\x00'

    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be'):
        # test surrogateescape
        s = "ab".encode(encoding, 'surrogateescape')
        s += b'\xff\xff'
        assert s.decode(encoding, 'surrogateescape') == 'ab\udcff\udcff'

        # test backslashreplace
        s = "ab".encode(encoding, 'backslash
