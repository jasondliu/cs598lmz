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

encoding = "utf-8"
print("Encoding:", encoding)

# Try this with and without U+DC00
print("\nDecode with add_one_codepoint")
encoded = b'\xf4\x90\x80\x00'
try:
    decoded = encoded.decode(encoding, "add_one_codepoint")
except UnicodeDecodeError as e:
    print(e)

print("\nDecode with add_utf16_bytes")
encoded = b'\x00'
try:
    decoded = encoded.decode(encoding, "add_utf16_bytes")
except UnicodeDecodeError as e:
    print(e)

print("\nDecode with add_utf32_bytes")
encoded = b'\x00'
try:
    decoded = encoded.decode(encoding, "add_utf32_bytes")
except UnicodeDecodeError as e:
    print(e)

print("\nEncode with add_one_codepoint")
try
