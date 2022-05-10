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

# tests for codecs.register_error

# doing a decode with a wrong error handler
try:
    unicode("abc", "ascii", "wrong_handler")
except LookupError:
    pass
else:
    print("expected LookupError")

# doing a encode with a wrong error handler
try:
    "abc".encode("ascii", "wrong_handler")
except LookupError:
    pass
else:
    print("expected LookupError")

# verify that the registered error handlers are working correctly
s = "abc\x80"
encoded = s.encode("latin-1", "add_one_codepoint")
if encoded != b"abca":
    print("expected b'abca', got", encoded)

decoded = encoded.decode("ascii", "add_one_codepoint")
if decoded != "abca":
    print("expected 'abca', got", decoded)

decoded = encoded.decode("utf-16-le", "add_utf16_bytes")
if dec
