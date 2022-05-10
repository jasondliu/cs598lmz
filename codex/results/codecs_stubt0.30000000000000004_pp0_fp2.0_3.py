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

# utf-16
print("utf-16")
s = "a"
s = s.encode("utf-16", "add_one_codepoint")
print(s)
s = s.decode("utf-16")
print(s)

# utf-32
print("utf-32")
s = "a"
s = s.encode("utf-32", "add_one_codepoint")
print(s)
s = s.decode("utf-32")
print(s)

# utf-16-le
print("utf-16-le")
s = "a"
s = s.encode("utf-16-le", "add_utf16_bytes")
print(s)
s = s.decode("utf-16-le")
print(s)

# utf-16-be
print("utf-16-be")
s = "a"
s = s.encode("utf-16-be", "add_utf16_bytes")
print(s)
s = s.decode("
