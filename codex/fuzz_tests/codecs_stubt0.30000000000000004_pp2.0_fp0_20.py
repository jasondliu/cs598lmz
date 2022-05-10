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

# test codecs.decode
for encoding in ["utf-8", "utf-16", "utf-32"]:
    print(encoding)
    assert codecs.decode(b"\x80", encoding, "strict") == "\uFFFD"
    assert codecs.decode(b"\x80", encoding, "replace") == "\uFFFD"
    assert codecs.decode(b"\x80", encoding, "ignore") == ""
    assert codecs.decode(b"\x80", encoding, "add_one_codepoint") == "a"
    assert codecs.decode(b"\x80", encoding, "add_utf16_bytes") == "\uFFFD"
    assert codecs.decode(b"\x80", encoding, "add_utf32_bytes") == "\uFFFD"

# test codecs.encode
for encoding in ["utf-8", "utf-16", "utf-32"]:
    print(encoding)
    assert codecs.encode("\uFFFD", encoding,
