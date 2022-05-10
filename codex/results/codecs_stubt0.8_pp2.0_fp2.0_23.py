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

# Test encoding

for enc in ('utf-8', 'utf-16', 'utf-32'):
    print("Encoding:", enc)
    print("  No errors")
    print("    ", repr(b'\xFC\x80\x80\x80'.decode(enc, 'strict')))
    print("    ", repr(b'\xFC\x80\x80\x80'.decode(enc, 'replace')))
    print("    ", repr(b'\xFC\x80\x80\x80'.decode(enc, 'ignore')))
    print("  Add one codepoint")
    print("    ", repr(b'\xFC\x80\x80\x80'.decode(enc, 'add_one_codepoint')))
    print("  Add n bytes")
    print("    ", repr(b'\xFC\x80\x80\x80'.decode(enc, 'add_utf16_bytes')))
    print("    ", repr(b'\xFC\x80\x80
