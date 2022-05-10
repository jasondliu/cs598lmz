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

u = chr(0xdc80)
utf8 = codecs.getencoder("utf-8")(u, "surrogateescape")[0]

assert u.encode("utf-8", "ignore") == b""
assert u.encode("utf-8", "replace") == b"\xef\xbf\xbd"
assert u.encode("utf-8", "xmlcharrefreplace") == b"&#56320;"
assert u.encode("utf-8", "backslashreplace") == b"\\U00100000"
assert u.encode("utf-8", "namereplace") == b"\\N{REPLACEMENT CHARACTER}"
assert u.encode("utf-8", "surrogateescape") == utf8
assert u.encode("utf-8", "add_one_codepoint") == b"a" + utf8
assert u.encode("utf-8", "add_utf16_bytes") == b"ab"
assert u.encode("utf-8", "add_utf32_
