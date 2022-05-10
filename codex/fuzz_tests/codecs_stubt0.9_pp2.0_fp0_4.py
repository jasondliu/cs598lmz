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

simple_ab = {u'a\U00012345b'.encode(encoding='utf-32'): 'utf-32',
             u'a\U00012345b'.encode(encoding='utf-16'): 'utf-16',
             u'a\U00012345b'.encode(encoding='utf-8'): 'utf-8'}

def test_add_one_codepoint():
    for bytes, encoding in simple_ab.items():
        dec_bytes = bytes.decode(encoding, 'add_one_codepoint')
        enc_dec_bytes = dec_bytes.encode(encoding)
        assert bytes.decode(encoding) in dec_bytes

def test_add_utf16_bytes():
    for bytes, encoding in simple_ab.items():
        dec_bytes = bytes.decode(encoding, 'add_utf16_bytes')
        assert u'aab\U00012345b' in dec_bytes
        enc_dec_bytes = dec_bytes.encode(encoding)
