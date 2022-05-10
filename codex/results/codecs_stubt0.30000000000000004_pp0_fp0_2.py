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

# Test the error handlers
print(u"\u1234".encode("ascii", "add_one_codepoint"))
print(u"\u1234".encode("utf-16", "add_utf16_bytes"))
print(u"\u1234".encode("utf-32", "add_utf32_bytes"))

# Test the error handlers with surrogates
print(u"\ud800\udc00".encode("ascii", "add_one_codepoint"))
print(u"\ud800\udc00".encode("utf-16", "add_utf16_bytes"))
print(u"\ud800\udc00".encode("utf-32", "add_utf32_bytes"))

# Test the error handlers with surrogates
print(u"\ud800\udc00\ud800\udc00".encode("ascii", "add_one_codepoint"))
print(u"\ud800\udc00\ud800\udc00".encode("utf-16", "add_utf
