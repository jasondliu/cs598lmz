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

for encoding in ("utf-8", "utf-16-le", "utf-16-be", "utf-32-le", "utf-32-be"):
    print("Encoding:", encoding)
    try:
        print("   ", codecs.getencoder(encoding)("\U000fffff"))
    except UnicodeEncodeError as exc:
        print("   ", exc.end - exc.start, "codepoints missing")
        print("   ", codecs.getencoder(encoding, "add_one_codepoint")("\U000fffff"))
    print()

print("Trying some UTF-16 encodings")
print(codecs.getencoder("utf-16-le", "add_one_codepoint")("\U000fffff"))
print(codecs.getencoder("utf-16-le", "add_utf16_bytes")("\U000fffff"))
try:
    print(codecs.getencoder("utf-16-le", "add_utf32_bytes")("\U000
