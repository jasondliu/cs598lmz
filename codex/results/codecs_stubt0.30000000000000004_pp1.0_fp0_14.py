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
    # Test UTF-16 and UTF-32 codecs
    for encoding in 'utf-16', 'utf-32':
        # Test decoding
        for error in 'strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes':
            for b in b'\xff', b'\xff\xff', b'\xff\xff\xff', b'\xff\xff\xff\xff':
                try:
                    s = b.decode(encoding, error)
                except UnicodeDecodeError:
                    pass
                else:
                    if error == 'strict':
                        raise TestFailed("decoding %r with error handler %s should have failed" % (b, error))
                    if error == 'add_one_codepoint' and encoding == 'utf-16':
                        assert s == 'a'
                    elif error == 'add_utf16_bytes' and encoding == 'utf-16':
                        assert s == 'ab'
                    elif error == 'add_utf
