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

data = "foo\xed\x95\x9c\xea\xb8\x80\xec\x9d\x98"
print("Start: " + repr(data))

print("as UTF-8: " + repr(data.encode("utf-8")))
print("as UTF-8 with replace: " + repr(
    data.encode("utf-8", "replace")))
print("as UTF-8 with add_one_codepoint: " + repr(
    data.encode("utf-8", "add_one_codepoint")))
print("as UTF-8 with add_utf16_bytes: " + repr(
    data.encode("utf-8", "add_utf16_bytes")))
print("as UTF-16 with add_one_codepoint: " + repr(
    data.encode("utf-16", "add_one_codepoint")))
print("as UTF-16 with add_utf16_bytes: " + repr(
    data.encode("utf-16", "add_utf16
