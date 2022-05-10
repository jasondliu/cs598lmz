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

# This test is for issue #1266.
def test_add_one_codepoint():
    u = '\u3042\u3044\u3046'
    b = b'\x82\xa0\x82\xa2\x82\xa4'
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint'):
            assert u.encode(encoding, errors) == b
            assert b.decode(encoding, errors) == u

# This test is for issue #1266.
def test_add_utf16_bytes():
    u = '\u3042\u3044\u3046'
    b = b'\x82\xa0\x82\xa2\x82\xa4'
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_utf16_bytes'):
            assert u.en
