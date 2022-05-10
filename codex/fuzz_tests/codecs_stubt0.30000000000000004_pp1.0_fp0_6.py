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

# test UnicodeEncodeError
for encoding in ('ascii', 'iso-8859-1', 'utf-8', 'utf-16', 'utf-32'):
    try:
        u"\u0100".encode(encoding)
    except UnicodeEncodeError as exc:
        print(encoding, exc.object, exc.start, exc.end)
        print(encoding, repr(exc.object[exc.start:exc.end]))
        print(encoding, repr(exc.object[exc.start:exc.end].encode(encoding, "replace")))
        print(encoding, repr(exc.object[exc.start:exc.end].encode(encoding, "backslashreplace")))
        print(encoding, repr(exc.object[exc.start:exc.end].encode(encoding, "xmlcharrefreplace")))
        print(encoding, repr(exc.object[exc.start:exc.end].encode(encoding, "add_one_codepoint")))
        print(encoding, repr(
