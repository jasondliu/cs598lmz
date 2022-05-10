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

utf8 = "abcdéfg"
utf16 = utf8.encode("utf_16")[2:]
utf32 = utf8.encode("utf_32")[4:]
mixed = utf8.encode("utf_7") + utf8[3:].encode("base64") + utf16[:3]

print("[UTF-8]", utf8)
print("[UTF-16]", utf16.decode("utf_16", "add_utf16_bytes"))
print("[UTF-32]", utf32.decode("utf_32", "add_utf32_bytes"))
print("[MIXED]", mixed.decode("utf_7", "add_one_codepoint").decode("base64"))
