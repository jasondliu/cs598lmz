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

def test_utf8():
    # UTF-8
    for i in range(0x100):
        if i in (0xC0, 0xC1):
            # Overlong encoding
            continue
        if i >= 0xF5:
            # Outside of the Unicode range
            continue
        if i >= 0xF0:
            # 4-byte sequence
            s = bytes([i, 0x80, 0x80, 0x80])
        elif i >= 0xE0:
            # 3-byte sequence
            s = bytes([i, 0x80, 0x80])
        elif i >= 0xC2:
            # 2-byte sequence
            s = bytes([i, 0x80])
        else:
            # Single byte
            s = bytes([i])
        try:
            s.decode('utf-8')
        except UnicodeDecodeError as exc:
            assert exc.object == s
            assert exc.start == 0
            assert exc.end == len(s)
            assert exc.reason == 'invalid start byte'

