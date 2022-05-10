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

# Test that the codecs module is working.
assert codecs.decode("\x80", "ascii", "add_one_codepoint") == "a\x80"
assert codecs.decode(b'\x80', "ascii", "add_utf16_bytes") == "a\x80"
assert codecs.decode(b'\x80', "ascii", "add_utf32_bytes") == "a\x80"

# Test that the codecs module is working with surrogate pairs.
assert codecs.decode("\xed\xa0\x80", "utf-8", "add_one_codepoint") == "a\ud800"
assert codecs.decode(b'\xed\xa0\x80', "utf-8", "add_utf16_bytes") == "a\ud800"
assert codecs.decode(b'\xed\xa0\x80', "utf-8", "add_utf32_bytes") == "a\ud800"

# Test that the codecs
