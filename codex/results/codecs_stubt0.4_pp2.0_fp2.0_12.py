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
    # test decoding with errors
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        codec = codecs.lookup(encoding)
        for b in (b'a\xff', b'a\xff\x00', b'a\xff\x00\x00'):
            for error in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                          'add_utf16_bytes', 'add_utf32_bytes'):
                try:
                    codec.decode(b, error)
                except UnicodeDecodeError as exc:
                    print(encoding, error, exc.object, exc.start, exc.end,
                          exc.reason)
                    if error == 'strict':
                        raise
                    elif error == 'ignore':
                        assert exc.end == len(b)
                    elif error == 'replace':
                        assert exc.end == len(b)
                    elif error == 'add_one_codepoint':
                        assert exc.end == len(
