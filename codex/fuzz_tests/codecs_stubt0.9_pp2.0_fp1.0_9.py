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

for encoding in "UTF-7 UTF-8 UTF-16 UTF-16LE UTF-16BE UTF-32 UTF-32LE UTF-32BE".split():
    codecs.decode(b"\xff", encoding, "replace")
    codecs.decode(b"\xff", encoding, "ignore")
    codecs.decode(b"\xff", encoding, "xmlcharrefreplace")
    codecs.decode(b"\xff", encoding, "backslashreplace")
    codecs.decode(b"\xff", encoding, "namereplace")
    codecs.decode(b"\xff", encoding, "add_one_codepoint")

# UTF-8 compatible decoders
for encoding in ['utf_7', 'utf-8']:
    codecs.decode(b"", encoding, "replace")
    codecs.decode(b"", encoding, "ignore")
    codecs.decode(b"", encoding, "xmlcharrefreplace")
    codecs.decode(b"", encoding, "backslashreplace")
   
