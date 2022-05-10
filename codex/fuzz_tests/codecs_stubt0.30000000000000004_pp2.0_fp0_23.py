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

def test_utf16_be_decoder():
    # test decoding surrogate pairs
    assert codecs.utf_16_be_decode(b'\xff\xfe\xd8\x00\xdc\x00', 'surrogatepass') == ('\U00010000', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\xd8\x00\xdc\x00', 'surrogateescape') == ('\ud800\udc00', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\xd8\x00\xdc\x00', 'ignore') == ('', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\xd8\x00\xdc\x00', 'replace') == ('?', 6)
    assert codecs.utf_16_be_decode(b'\xff\xfe\xd8\x00\xdc\x00', 'add_one_codepoint') ==
