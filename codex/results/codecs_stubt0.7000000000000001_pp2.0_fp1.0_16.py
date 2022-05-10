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

inputs = [
    # bytes, decoding error handler, expected output
    (b'\xc4\x85', "add_one_codepoint", "aa"),
    (b'\xc4\x85', "add_utf16_bytes", "aba"),
    (b'\xc4\x85', "add_utf32_bytes", "abcd"),
    (b'\xc4\x85', "strict", None),
    (b'\xc4\x85', "ignore", ""),
    (b'\xc4\x85', "replace", "\ufffd"),
    (b'\xc4\x85', "xmlcharrefreplace", "&#261;"),
    (b'\xc4\x85', "backslashreplace", "\\xc4\\x85"),
    (b'\xc4\x85', "callback", TypeError),
]

for i in inputs:
    bytes, handler, expected = i
    try:
        result = bytes.decode("utf-8", handler)
    except Exception as e:

