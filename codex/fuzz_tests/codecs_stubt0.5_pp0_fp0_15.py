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
    # Surrogates
    for s in [
        u'\ud800',
        u'\udc00',
        u'\ud800\udc00',
        u'\udbff\udfff',
        u'\ud800\udbff\udfff',
        ]:
        for encoding in 'utf-8', 'utf-16', 'utf-32':
            for errors in 'strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes':
                try:
                    codecs.encode(s, encoding, errors)
                except UnicodeEncodeError:
                    pass
                else:
                    print("expected exception for encoding", encoding, errors)

    # non-BMP
    for s in [
        u'\U00010000',
        u'\U00010000\U00010000',
        u'\U0010ffff',
        u'\U00010000\U0010ffff',
        ]:
        for encoding in 'utf-8
