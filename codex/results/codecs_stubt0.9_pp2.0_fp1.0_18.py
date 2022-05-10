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

handlers = (
    "add_one_codepoint",
    "add_utf16_bytes",
    "add_utf32_bytes",
    "xmlcharrefreplace",
    "strict",
    "replace",
    "ignore",
    )

def test(encoding):
    if encoding == "utf-16":
        # We use byteorder '<' for little-endian orders because
        # that "just works"
        s = b'\xff\xfeA\x00B\x00C\x00D\x00'
    elif encoding == "utf-16-be":
        s = b'\xfe\xff\x00A\x00B\x00C\x00D'
    elif encoding == "utf-32":
        s = b'\xff\xfe\x00\x00\x00A\x00\x00\x00B\x00\x00\x00C\x00\x00\x00D'
    elif encoding == "utf-32-be":
        s
