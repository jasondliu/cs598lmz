import codecs
# Test codecs.register_error
x = "\\x80".encode("ascii", "strict")
assert x == b"\\x80"

# Test PyUnicode_GetDefaultEncoding
assert "".encode() == b""
