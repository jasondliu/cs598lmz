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

for encoding in ['utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be']:
    # With replacement
    u8 = 'abc\xff'.encode(encoding, 'add_one_codepoint')
    assert u8 == 'abc\xffa'.encode(encoding)
    # With replacement but bytes
    u8 = 'abc\xff'.encode(encoding, 'add_utf16_bytes')
    assert u8 == b'ab\xffab'.encode(encoding)
    # With replacement but bytes
    u8 = 'abc\xff'.encode(encoding, 'add_utf32_bytes')
    assert u8 == b'ab\xffabcd'.encode(encoding)
