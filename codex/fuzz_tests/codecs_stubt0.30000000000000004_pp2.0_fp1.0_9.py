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

# Test that UTF-16 and UTF-32 codecs can be used to decode surrogate pairs
# and non-BMP characters.

for encoding in "utf-16", "utf-32":
    for errors in "strict", "replace", "ignore", "add_one_codepoint", \
                  "add_utf16_bytes", "add_utf32_bytes":
        for data in b'\x00\xD8\x00\xDC', b'\x00\xDC\x00\xD8', \
                    b'\x00\xD8\x00\xDC\x00\xD8\x00\xDC', \
                    b'\x00\xDC\x00\xD8\x00\xDC\x00\xD8', \
                    b'\x00\xD8\x00\xDC\x00\xDC\x00\xD8', \
                    b'\x00\xDC\x00\xD8\x00\xD8\x00\xDC', \

