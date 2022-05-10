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

# Test UTF-8

# Test decoding with errors
assert codecs.decode("\xff", "utf-8", "strict") == "\ufffd"
assert codecs.decode("\xff", "utf-8", "replace") == "\ufffd"
assert codecs.decode("\xff", "utf-8", "ignore") == ""
assert codecs.decode("\xff", "utf-8", "add_one_codepoint") == "a"
assert codecs.decode("\xff", "utf-8", "add_utf16_bytes") == "\ufffd"
assert codecs.decode("\xff", "utf-8", "add_utf32_bytes") == "\ufffd"

# Test encoding with errors
assert codecs.encode("\u1234", "utf-8", "strict") == b"\xe1\x88\xb4"
assert codecs.encode("\u1234", "utf-8", "replace") == b"\xef\xbf\xbd"
assert codecs.encode("
