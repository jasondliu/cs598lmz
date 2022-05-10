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
        for error_handler in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for input in ('abc', '\u1234', '\ud800', '\udc00', '\ud800\udc00', '\ud800\udc00\ud800\udc00', '\ud800\udc00\ud800\udc00\ud800\udc00'):
                try:
                    output = input.encode(encoding, error_handler)
                except UnicodeEncodeError:
                    pass
                else:
                    try:
                        output.decode(encoding, error_handler)
                    except UnicodeDecodeError:
                        pass

if __name__ == "__main__":
    test_main()
