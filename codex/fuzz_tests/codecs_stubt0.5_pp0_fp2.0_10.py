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

data = b'\x00\x00\x00'

for encoding in ('ascii', 'utf-8', 'utf-16', 'utf-32'):
    print(encoding)
    try:
        data.decode(encoding)
    except UnicodeDecodeError as exc:
        print(exc)
        print(exc.object)
        print(exc.object.decode(encoding, 'add_one_codepoint'))
        print(exc.object.decode(encoding, 'add_utf16_bytes'))
        print(exc.object.decode(encoding, 'add_utf32_bytes'))
    print()
