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
    for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'backslashreplace',
                       'xmlcharrefreplace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            yield check_decode, encoding, errors
            yield check_encode, encoding, errors

def check_decode(encoding, errors):
    s = b'\x80'
    u = s.decode(encoding, errors)
    if errors == 'add_one_codepoint':
        assert u == 'a\uFFFD'
    elif errors == 'add_utf16_bytes':
        assert u == 'a\uFFFD'
    elif errors == 'add_utf32_bytes':
        assert u == 'a\uFFFD'
    else:
        assert u == s.decode(encoding, 'strict')

