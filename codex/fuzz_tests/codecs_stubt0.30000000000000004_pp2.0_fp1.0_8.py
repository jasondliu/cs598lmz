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
        for errors in ('strict', 'replace', 'ignore',
                       'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            print("testing encoding", encoding, "with errors", errors)
            try:
                codecs.decode(b'\xff', encoding, errors)
            except UnicodeDecodeError as exc:
                print("UnicodeDecodeError:", exc.reason, exc.object[exc.start:exc.end])
            else:
                print("No exception")

test_main()
