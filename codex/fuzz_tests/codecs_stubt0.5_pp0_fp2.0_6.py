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

# This test is for bug #1536.

for encoding in ['utf-8', 'utf-16', 'utf-32']:
    for error_handler in ['strict', 'replace', 'ignore', 'add_one_codepoint',
                          'add_utf16_bytes', 'add_utf32_bytes']:
        print(encoding, error_handler)
        # Encode a string and decode it back.
        s = '\u1234'
        t = s.encode(encoding, error_handler)
        u = t.decode(encoding, error_handler)
        print(repr(u))
        print(repr(s))
        assert u == s

        # Try encoding a string with a character that can't be encoded.
        try:
            s = '\u1234\uFFFF'
            t = s.encode(encoding, error_handler)
        except UnicodeEncodeError:
            pass
        else:
            assert error_handler in ['replace', 'ignore', 'add_one_codepoint',

