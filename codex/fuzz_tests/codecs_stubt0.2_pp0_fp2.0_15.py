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
    # Test UTF-8
    for i in range(0, 0xd800):
        # Encode single character
        if i == 0 or 0xd800 <= i <= 0xdfff or i > 0x10ffff:
            # Illegal character
            raises(UnicodeEncodeError, '\u%04x' % i, 'utf-8')
        else:
            assert '\u%04x' % i == '\u%04x' % i.encode('utf-8').decode('utf-8')

        # Encode surrogate pair
        if 0xd800 <= i <= 0xdbff:
            s = '\u%04x\u%04x' % (i, 0xdc00 + (i & 0x3ff))
            assert s == s.encode('utf-8').decode('utf-8')

    # Test UTF-16
    for i in range(0, 0x110000):
        # Encode single character
        if i == 0 or 0xd800 <= i <= 0xdfff or i > 0x10
