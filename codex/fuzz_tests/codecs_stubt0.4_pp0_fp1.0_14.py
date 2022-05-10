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

print(u"\u3042".encode("utf-16", "add_one_codepoint"))
print(u"\u3042".encode("utf-32", "add_one_codepoint"))

print(b"\x42\x30".decode("utf-16", "add_utf16_bytes"))
print(b"\x42\x30\x00\x00".decode("utf-32", "add_utf32_bytes"))

print(u"\u3042".encode("utf-16", "surrogatepass"))
print(u"\u3042".encode("utf-32", "surrogatepass"))

print(b"\x42\x30".decode("utf-16", "surrogatepass"))
print(b"\x42\x30\x00\x00".decode("utf-32", "surrogatepass"))

print(u"\u3042".encode("utf-16", "surrogateescape"))
print(u"\u3042".encode("
