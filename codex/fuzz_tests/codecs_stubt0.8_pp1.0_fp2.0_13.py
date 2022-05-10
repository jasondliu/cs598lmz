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

def print_decoded(s, encoding):
    print("%r encoded as %s decodes to %r" %
          (s, encoding, codecs.decode(s, encoding)))

S = b"\xff\xfe\x00\x00\x61\x00\x00\x00"
# bytes to decode: one invalid codepoint
print_decoded(S, "utf-16")
print_decoded(S, "utf-16-le")
print_decoded(S, "utf-16-be")
print_decoded(S, "utf-32")
print_decoded(S, "utf-32-le")
print_decoded(S, "utf-32-be")

print("\nUsing the <escape> handler:")
print_decoded(S, "utf-16", "replace")
print_decoded(S, "utf-16-le", "replace")
print_decoded(S, "utf-16-be", "replace")
print_decoded(S, "utf-32", "replace")
