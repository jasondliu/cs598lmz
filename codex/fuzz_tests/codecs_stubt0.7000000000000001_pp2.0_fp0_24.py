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


tests = [
    (b'\xff', 'add_one_codepoint', "utf-8",  'a\xff', 1),
    (b'\xff', 'add_utf16_bytes', "utf-8",  'ab\xff', 3),
    (b'\xff', 'add_utf32_bytes', "utf-8",  'abcd\xff', 7),
    (b'\xff\xff', 'add_one_codepoint', "utf-8",  'a\xff\xff', 1),
    (b'\xff\xff', 'add_utf16_bytes', "utf-8",  'ab\xff\xff', 3),
    (b'\xff\xff', 'add_utf32_bytes', "utf-8",  'abcd\xff\xff', 7),

    (b'\xff', 'add_one_codepoint', "utf-16-le",  'a\xff', 1),
    (b'\xff', 'add_utf16_bytes', "utf-16-le",  'ab\xff
