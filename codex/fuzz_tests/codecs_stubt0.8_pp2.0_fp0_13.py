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

def one_utf16_to_one_codepoint(exc):
    if len(exc.object) != 2:
        return
    return (unichr(ord(exc.object[0]) << 8 | ord(exc.object[1])),
            exc.end)

def two_utf16_to_one_codepoint(exc):
    if len(exc.object) != 4:
        return
    return (unichr(ord(exc.object[0]) << 8 | ord(exc.object[1])),
            exc.end)

def one_utf32_to_one_codepoint(exc):
    if len(exc.object) != 4:
        return
    codepoint = (ord(exc.object[0]) << 24 | ord(exc.object[1]) << 16 |
                 ord(exc.object[2]) << 8 | ord(exc.object[3]))
    if 0x10000 <= codepoint <= 0x10ffff:
        return (unichr(codepoint), exc.end)

def two_
