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

# UTF-16
assert codecs.decode("\x00\x00\x00", "utf-16", errors="replace") == u'\ufffd'
assert codecs.decode("\x00\x00\x00", "utf-16", errors="ignore") == u''
assert codecs.decode("\x00\x00\x00", "utf-16", errors="add_one_codepoint") == u'\ufffd'
assert codecs.decode("\x00\x00\x00", "utf-16", errors="add_utf16_bytes") == u'a\ufffd'
assert codecs.decode("\x00\x00\x00", "utf-16", errors="add_utf32_bytes") == u'a\ufffd'

# UTF-32
assert codecs.decode("\x00\x00\x00\x00", "utf-32", errors="replace") == u'\ufffd'
assert codecs.decode("\x00\x00\x00\x00", "
