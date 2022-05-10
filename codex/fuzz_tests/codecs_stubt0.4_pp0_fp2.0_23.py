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
    # Verify that the codecs module can be used to encode/decode
    # Unicode strings.
    for encoding in ('latin-1', 'utf-8', 'utf-16', 'utf-32'):
        for s in ('abc', '\xe4\xf6\xfc', '\u20ac', '\U0001d120'):
            for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                           'add_utf16_bytes', 'add_utf32_bytes'):
                encoded = s.encode(encoding, errors)
                decoded = encoded.decode(encoding, errors)
                if errors == 'strict':
                    assert s == decoded
                else:
                    assert s.encode(encoding, 'strict') == encoded
                assert s == decoded

    # Verify that the codecs module can be used to encode/decode
    # 8-bit strings.
    for encoding in ('latin-1', 'utf-8', 'utf-16', 'utf
