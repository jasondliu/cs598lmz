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

def test_encoding_errors(fn):
    # Fails with:
    # UnicodeDecodeError: 'utf8' codec can't decode bytes in position 0-1: invalid continuation byte
    # or:
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0x99 in position 0: invalid start byte
    # or:
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0x84 in position 0: unexpected code byte
    # or:
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0x80 in position 0: invalid start byte
    with pytest.raises(UnicodeDecodeError):
        fn(b'\x80')

    with pytest.raises(UnicodeDecodeError):
        fn(b'\x81')

    with pytest.raises(UnicodeDecodeError):
        fn(b'\x84')

    with pytest.raises(UnicodeDecodeError):
        fn(b'\x99')

    with pytest.raises(Un
