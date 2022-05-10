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

def test():
    # issue #14371
    for encoding in 'utf-16', 'utf-32':
        with open(TESTFN, 'wb') as f:
            f.write(b'a\x00\x00\x00b') # 'a' + U+0000
        with open(TESTFN, 'rb') as f:
            text = f.read().decode(encoding, 'add_one_codepoint')
        assert text == 'aa'
        with open(TESTFN, 'wb') as f:
            f.write(b'\x00\x61\x00\x00\x00\x00\x00\x62') # U+0000 + 'a'
        with open(TESTFN, 'rb') as f:
            text = f.read().decode(encoding, 'add_one_codepoint')
        assert text == 'aa'
    for encoding in 'utf-16-be', 'utf-16-le', 'utf-32-be', 'utf-32-le':
        with open
