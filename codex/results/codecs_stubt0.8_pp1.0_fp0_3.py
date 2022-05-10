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

with codecs.open(__file__, encoding="ascii", errors="add_one_codepoint") as f:
    print(repr(f.read()))

with codecs.open(__file__, encoding="utf-16", errors="add_utf16_bytes") as f:
    print(repr(f.read()))

with codecs.open(__file__, encoding="utf-32", errors="add_utf32_bytes") as f:
    print(repr(f.read()))
