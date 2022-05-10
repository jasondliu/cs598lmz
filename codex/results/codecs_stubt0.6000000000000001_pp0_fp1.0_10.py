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

print("\nTesting UTF-32 codec\n")

for encoding in [ "utf-32", "utf-32-le", "utf-32-be"]:
    print("Encoding:", encoding)
    print("Encoding:", encoding, "with surrogateescape")
    print("Encoding:", encoding, "with replace")
    print("Encoding:", encoding, "with add_one_codepoint")
    print("Encoding:", encoding, "with add_utf32_bytes")
    print("Decoding:", encoding)
    print("Decoding:", encoding, "with surrogateescape")
    print("Decoding:", encoding, "with replace")

print("\nTesting UTF-32-exotic codec\n")

for encoding in [ "utf-32-exotic", "utf-32-exotic-le", "utf-32-exotic-be"]:
    print("Encoding:", encoding)
    print("Encoding:", encoding, "with surrogateescape")
    print("Encoding:", encoding, "with replace")
    print("Encoding:
