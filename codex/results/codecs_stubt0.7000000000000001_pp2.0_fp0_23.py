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

u = chr(0xFFFE)

# first test with Latin-1, add_one_codepoint
for name in [ "latin_1", "iso8859_1", "8859" ]:
    encoding = name
    try:
        encoded = u.encode(encoding)
    except UnicodeEncodeError as exc:
        print("UnicodeEncodeError:", exc.reason)
        print("with", encoding, ":", repr(exc.object))
        print("encoding with 'add_one_codepoint'...")
        encoded = u.encode(encoding, "add_one_codepoint")
        print("encoded:", repr(encoded))
    else:
        print("encoded without failure:", repr(encoded))
    try:
        decoded = encoded.decode(encoding)
    except UnicodeDecodeError as exc:
        print("UnicodeDecodeError:", exc.reason)
        print("with", encoding, ":", repr(exc.object))
        print("encoding with
