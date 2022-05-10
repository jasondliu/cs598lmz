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

print("\n   Decoding errors:")
for encoding in ['ascii', 'utf-8', 'utf-16', 'utf-32']:
    print("\n  ", encoding)
    for error_handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
        try:
            print("    ", error_handler, ":", bytes(b"\xff").decode(encoding, errors=error_handler))
        except UnicodeDecodeError as exc:
            print("    ", error_handler, ":", exc)

print("\n   Encoding errors:")
for encoding in ['ascii', 'utf-8', 'utf-16', 'utf-32']:
    print("\n  ", encoding)
    for error_handler in ["strict", "ignore", "replace"]:
        try:
            print("    ", error_handler, ":", "\u1234".encode(encoding, errors=error_handler))
        except UnicodeEn
