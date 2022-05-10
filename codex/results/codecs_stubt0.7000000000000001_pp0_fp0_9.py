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


import unicodedata as ud

def misc_chars(c):
    return (0x0000 <= ord(c) <= 0x0020 or
            0x007F <= ord(c) <= 0x009F or
            ord(c) == 0x200D or
            ord(c) == 0x200C or
            ud.decimal(c, -1) >= 0 or
            c in '\u06DD\u06DE\u06DF' or
            0xE0100 <= ord(c) <= 0xE01EF)


def is_ambiguous_width(c):
    return ud.east_asian_width(c) == 'A'


def is_fullwidth(c):
    return ud.east_asian_width(c) == 'F'


def is_halfwidth(c):
    return ud.east_asian_width(c) == 'H'


def is_narrow(c):
    return ud.east_asian_width(c) == 'Na'


def is_wide
