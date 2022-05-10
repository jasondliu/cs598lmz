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


# Try all combinations of unicode, bytes and bytearray, for both encoding and
# decoding.
for enc, errors in [
        ("utf-8", "surrogateescape"),
        ("utf-16", "add_utf16_bytes"),
        ("utf-32", "add_utf32_bytes"),
        # The following are currently not supported, but they should be
        # supported one day.
        #("utf-7", "add_utf16_bytes"),
        #("utf-8-sig", "add_utf16_bytes"),
        ]:
    for input in [b'abc', 'abc', bytearray(b'abc')]:
        for encoding in [enc, enc.encode('ascii')]:
            for errors in ["strict", "ignore", errors]:
                try:
                    codecs.decode(input, encoding, errors)
                except UnicodeDecodeError as exc:
                    pass
                else:
                    raise Exception("Should have raised UnicodeDecodeError")
            for output in [b'abc', 'abc', bytearray
