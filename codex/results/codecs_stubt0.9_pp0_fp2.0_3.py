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

# In addition, you can provide the maximum and an alternate
# unicode character to represent the codepoint:

def alt_character(exc):
    return (u'\ufffd', exc.end)

codecs.register_error("alt_character", alt_character)

def max_char(exc):
    return (u'\U0010FFFF', exc.end)

codecs.register_error("max_character", max_char)

for enc in ("utf-8", "utf-16", "utf-32"):
    print("%s:" % enc)
    # test a Replacer error handler:
    codecs.register_error("ignore", codecs.ignore_errors)
    char = codecs.decode(b"abcde", enc)
    print("  ignore_errors: %r (%r)" % (char, char.encode(enc)))

    # test an Insert/InsertStr error handler:
    codecs.register_error("add_one_codepoint", add_one_codepoint)
    char = codecs.dec
