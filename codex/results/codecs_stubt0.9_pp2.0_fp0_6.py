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

# UTF-16 surrogate pair for U+10FFFF
u16 = "\\xD8\\x10\\xDB\\xFF".decode("unicode-escape")

# UTF-32 surrogate pair for U+10FFFF
u32 = "\\x00\\x01\\x00\\x0F\\x00\\x00\\xDB\\xFF".decode("unicode-escape")

#

val = chr(0xDC80)*2
print "original unicode string:", repr(val)

# Try to encode it.
for encoding in "latin-1", "utf-8", "utf-16", "utf-16-le":
    print "trying encoding:", encoding
    # this must raise an UnicodeEncodeError
    try:
        print "encode:", repr(val.encode(encoding))
    except ValueError, v:
        print "couldn't encode:", str(v)
    # let's add one codepoint before reporting
    # about the error
    print "encode (with add_one_codepoint):
