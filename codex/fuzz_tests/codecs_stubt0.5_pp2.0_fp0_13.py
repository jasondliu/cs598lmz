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

# Test the UTF-16 codec
for encoding in "utf-16-be", "utf-16-le", "utf-16":
    # Test the error handler
    s = b'\x00\x00\x00\x00'
    s.decode(encoding, "add_one_codepoint")

    # Test the incremental decoder
    d = codecs.getincrementaldecoder(encoding)()
    d.decode(b'\x00\x00\x00')
    d.decode(b'\x00', "add_one_codepoint")

    # Test the incremental encoder
    e = codecs.getincrementalencoder(encoding)()
    e.encode("\x00")
    e.encode("\x00\x00", "add_one_codepoint")

# Test the UTF-32 codec
for encoding in "utf-32-be", "utf-32-le", "utf-32":
    # Test the error handler
    s = b'\x00\x00\
