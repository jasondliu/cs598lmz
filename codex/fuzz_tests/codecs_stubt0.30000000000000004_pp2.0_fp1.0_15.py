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
for encoding in ('ascii', 'iso-8859-1', 'utf-8', 'utf-16-be', 'utf-32-be'):
    print(encoding)
    try:
        '\ud800'.encode(encoding)
    except UnicodeEncodeError as exc:
        print(repr(exc))
        print(exc.object)
        print(exc.start)
        print(exc.end)
        print(exc.reason)
        print(exc.encoding)
        print(exc.object[exc.start:exc.end])
        print(exc.encode("ascii", "backslashreplace"))
        print(exc.encode("ascii", "namereplace"))
        print(exc.encode("ascii", "replace"))
        print(exc.encode("ascii", "xmlcharrefreplace"))
        print(exc.encode("ascii", "add_one_codepoint"))
        print(exc.encode("ascii", "add_utf
