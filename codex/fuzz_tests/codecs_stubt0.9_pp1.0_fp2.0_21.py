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

# latin-1:       0x00 0x7f
# utf-16-le:   0x00 0x00  0xff 0xff
# utf-16-be:   0x00 0x00  0xff 0xff
# utf-32-le: 0x00 0x00 0x00 0x00  0xff 0xff 0xff 0xff
# utf-32-be: 0x00 0x00 0x00 0x00  0xff 0xff 0xff 0xff
ASCII = b"9"
NUNICO = b"\xF2"

for encoding in ('iso-8859-1', 'utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be'):
    # ok
    print("'{}' encoding:".format(encoding))
    print("  ok |", end=' ')
    # in bytes
    print("{:2d} |".format(len(ASCII)), codecs.decode(ASCII, encoding, 'strict'))
    # in
