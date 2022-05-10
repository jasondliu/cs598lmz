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

print(u'abc\u0e00\ud800\udfff\U00010000'.encode("ascii", "add_one_codepoint"))
print(u'\ud800\udfff\U00010000'.encode("utf-16-le", "add_utf16_bytes"))
print(u'\ud800\udfff\U00010000'.encode("utf-32-le", "add_utf32_bytes"))
