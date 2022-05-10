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
    # Test the BOM
    for (bom, encoding) in [
        (b'\x00\x00\xfe\xff', 'utf-32-be'),
        (b'\xff\xfe\x00\x00', 'utf-32-le'),
        (b'\xfe\xff', 'utf-16-be'),
        (b'\xff\xfe', 'utf-16-le'),
        (b'\xef\xbb\xbf', 'utf-8'),
    ]:
        s = bom + b'abc'
        assert s.decode(encoding) == 'abc'
        assert s.decode(encoding, 'ignore') == ''
        assert s.decode(encoding, 'replace') == bom.decode('ascii') + 'abc'
        assert s.decode(encoding, 'add_one_codepoint') == bom.decode('ascii') + 'aabc'
        assert s.decode(encoding, 'add_utf16_bytes
