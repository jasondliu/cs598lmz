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

# test utf-8
for enc in ["utf-8", "utf_8"]:
    for error in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"]:
        for i in range(0, 256):
            try:
                codecs.decode(bytes([i]), enc, error)
            except UnicodeDecodeError as e:
                print(enc, error, i, e)

# test utf-16
for enc in ["utf-16", "utf_16"]:
    for error in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"]:
        for i in range(0, 256):
            try:
                codecs.decode(bytes([i, 0]), enc, error)
            except UnicodeDecodeError as e:
                print(enc, error, i, e)

# test utf-32
for enc in ["utf-32", "utf_32"]:
    for error in ["strict", "replace",
