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

def test_codecs_add_one_codepoint():
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for bad_codepoint in (b'\x80', b'\x80\x80', b'\x80\x80\x80\x80'):
            s = codecs.decode(bad_codepoint, encoding, "replace")
            assert s == '\ufffd'
            s = codecs.decode(bad_codepoint, encoding, "ignore")
            assert s == ''
            s = codecs.decode(bad_codepoint, encoding, "add_one_codepoint")
            assert s == 'a'
            s = codecs.decode(bad_codepoint, encoding, "add_utf16_bytes")
            assert s == 'ab'
            s = codecs.decode(bad_codepoint, encoding, "add_utf32_bytes")
            assert s == 'abcd'

def test_codecs_decode_error():
