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

# Test for issue #8131
def test_utf16_decode_error():
    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be'):
        for b in (b'\xff', b'\xff\xff', b'\xff\xff\xff'):
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding)
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding, 'strict')
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding, 'replace')
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding, 'ignore')
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding, 'xmlcharrefreplace')
            with pytest.raises(UnicodeDecodeError):
                b.decode(encoding, 'backslashreplace')
            with
