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

encode_tests = [
        # invalid start byte
        (b'\x80', 'add_one_codepoint', '\u0080'),
        (b'\x80', 'add_utf16_bytes', '\u0080'),
        (b'\xc0\x80', 'add_one_codepoint', '\u0000'),
        (b'\xc0\x80', 'add_utf16_bytes', '\u0000'),
        (b'\xe0\x80\x80', 'add_one_codepoint', '\u0000'),
        (b'\xe0\x80\x80', 'add_utf16_bytes', '\u0000'),
        (b'\xf0\x80\x80\x80', 'add_one_codepoint', '\u0000'),
        (b'\xf0\x80\x80\x80', 'add_utf32_bytes', '\u0000'),
        (b'\xf0\x80\x80', 'add_one_codepoint
