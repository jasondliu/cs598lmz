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

# test utf-16
for errors in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes"]:
    for encoding in ["utf-16", "utf-16-le", "utf-16-be"]:
        print(errors, encoding)
        u = chr(0xdc00)
        for i in range(1, 10):
            u += chr(0xd800) + chr(0xdc00)
        print(u.encode(encoding, errors))
        print(u.encode(encoding, errors).decode(encoding, errors))

# test utf-32
for errors in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf32_bytes"]:
    for encoding in ["utf-32", "utf-32-le", "utf-32-be"]:
        print(errors, encoding)
        u = chr(0xdc00)
        for i in range(1, 10):
            u += chr(
