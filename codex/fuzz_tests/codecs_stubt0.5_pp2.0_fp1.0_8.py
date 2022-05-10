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

# UTF-8
print(codecs.decode("\xFF", "utf-8", "add_one_codepoint"))
print(codecs.encode("\uDC80", "utf-8", "add_one_codepoint"))

# UTF-16
print(codecs.decode(b"\xFF\xFF", "utf-16", "add_utf16_bytes"))
print(codecs.encode("\uDC80", "utf-16", "add_utf16_bytes"))

# UTF-32
print(codecs.decode(b"\xFF\xFF\xFF\xFF", "utf-32", "add_utf32_bytes"))
print(codecs.encode("\uDC80", "utf-32", "add_utf32_bytes"))

# Big5
print(codecs.decode(b"\xFF", "big5", "add_one_codepoint"))
print(codecs.encode("\uDC80", "big5", "
