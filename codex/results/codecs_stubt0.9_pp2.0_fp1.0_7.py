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

print(codecs.encode("Hello World", "utf-16", "ignore"))
print(codecs.encode("Hello World", "utf-16", "add_one_codepoint"))
print(codecs.encode("Hello World", "utf-16", "add_utf16_bytes"))
print(codecs.encode("Hello World", "utf-16", "add_utf32_bytes"))

print(codecs.encode("Hello World", "utf-32", "add_utf16_bytes"))
print(codecs.encode("Hello World", "utf-32", "add_utf32_bytes"))

print(codecs.decode(b"ab", "utf-16"))
print(codecs.decode(b"ab", "utf-32"))

print(codecs.decode(b"ab", "utf-16", "ignore"))
print(codecs.decode(b"ab", "utf-16", "ignore"), "utf-16-be", "replace")
print(codecs.
