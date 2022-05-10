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

def test_main():
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            print(encoding, errors)
            try:
                codecs.decode(b'\xff', encoding, errors)
            except UnicodeDecodeError as e:
                print(e)
                print(e.object)
                print(e.start)
                print(e.end)
                print(e.reason)
                print(e.object[e.start:e.end])
                print(e.encode('ascii', 'backslashreplace'))
                print(repr(e))
                print(str(e))
                print()

test_main()
