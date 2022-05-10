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

# Test UTF-8

print("UTF-8")

print("strict")
try:
    codecs.decode("\x80", "utf-8")
except UnicodeDecodeError as exc:
    print(exc)

print("replace")
print(codecs.decode("\x80", "utf-8", "replace"))

print("ignore")
print(codecs.decode("\x80", "utf-8", "ignore"))

print("add_one_codepoint")
print(codecs.decode("\x80", "utf-8", "add_one_codepoint"))

print("add_utf16_bytes")
try:
    codecs.decode("\x80", "utf-8", "add_utf16_bytes")
except UnicodeDecodeError as exc:
    print(exc)

print("add_utf32_bytes")
try:
    codecs.decode("\x80", "utf-8", "add_utf32_bytes")
except UnicodeDecodeError as exc:
