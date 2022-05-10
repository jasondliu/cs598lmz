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

# invalid UTF-8
s = b"\xFF"

# decode
u = s.decode("utf-8", "ignore")
print(u)

u = s.decode("utf-8", "replace")
print(u)

u = s.decode("utf-8", "add_one_codepoint")
print(u)

u = s.decode("utf-8", "add_utf16_bytes")
print(u)

u = s.decode("utf-8", "add_utf32_bytes")
print(u)

# encode
s = u.encode("utf-8", "ignore")
print(s)

s = u.encode("utf-8", "replace")
print(s)

s = u.encode("utf-8", "add_one_codepoint")
print(s)

s = u.encode("utf-8", "add_utf16_bytes")
print(s)

s = u.encode("utf-8", "add_utf
