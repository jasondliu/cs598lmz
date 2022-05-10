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

def encdec(encoding):
    for byte in u"\u4242\U00022222".encode(encoding, "add_one_codepoint").decode(encoding):
        print(repr(byte))

print(u"codepoints")
encdec("utf-16")
encdec("utf-16-le")
encdec("utf-16-be")
encdec("utf-16-ex")
encdec("utf-16-le-ex")
encdec("utf-16-be-ex")
encdec("utf-32")
encdec("utf-32-le")
encdec("utf-32-be")
encdec("utf-32-ex")
encdec("utf-32-le-ex")
encdec("utf-32-be-ex")

def encdec(encoding):
    te = "ab".encode(encoding, "add_utf16_bytes")
    for byte in te.decode(encoding):
        print(repr(byte))
