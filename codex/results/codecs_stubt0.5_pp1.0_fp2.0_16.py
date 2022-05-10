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

# test encoding
encoding = "utf-16-le"

for name, error in [("strict", None),
                    ("ignore", "ignore"),
                    ("replace", "replace"),
                    ("add_one_codepoint", "add_one_codepoint"),
                    ("add_utf16_bytes", "add_utf16_bytes"),
                    ("add_utf32_bytes", "add_utf32_bytes")]:
    print("encoding error handler:", name)
    print("%r" % unicode("abc\x81\x00", encoding, error))
    print("%r" % unicode("abc\x81\x00\x00\x00", encoding, error))
    print()
