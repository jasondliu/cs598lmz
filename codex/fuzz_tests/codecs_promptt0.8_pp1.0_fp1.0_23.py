import codecs
# Test codecs.register_error
x = "\\x80".encode("ascii", "strict")
assert x == b"\\x80"

# Test PyUnicode_GetDefaultEncoding
assert "".encode() == b""
assert b"\xe9".decode() == "\xe9"

# Test codecs.register_error
assert codecs.register_error("strict", lambda e: ("", e.end))
x = "\\x80".encode("ascii", "strict")
assert x == b""

# Test codecs.lookup_error
assert codecs.lookup_error("strict")[0] is codecs.strict_errors
assert codecs.lookup_error("ignore")[0] is codecs.ignore_errors
assert codecs.lookup_error("replace")[0] is codecs.replace_errors
assert codecs.lookup_error("xmlcharrefreplace")[0] is codecs.xmlcharrefreplace_errors
assert codecs.lookup_error("backslashreplace")[0] is codecs.backsl
