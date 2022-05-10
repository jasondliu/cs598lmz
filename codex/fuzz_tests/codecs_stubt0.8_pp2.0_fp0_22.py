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

def test_utf7(check_backslashes):
    encodings = ("utf_7", "utf_16", "utf_32")
    errorhandlers = ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes")
    #
    # Build a string that has a lot of characters pretty far into the BMP,
    # and then add a character with a very high code point.  We need to
    # have some characters that aren't in the basic multilingual plane
    # because they're handled differently in UTF-7.
    #
    # The string has to end with '+' or '+-', otherwise it'll be
    # interpreted in UTF-7 as having more characters to come, even if
    # the next character is '-'.
    #
    # The '+' must be escaped, otherwise it'll be interpreted as the
    # beginning of a UTF-7 sequence even if the next character is '-'.
    #
    big_unicode_char = 0x10FFFF
    s
