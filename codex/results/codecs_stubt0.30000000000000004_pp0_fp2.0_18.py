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
    # test utf-16-le
    utf16_le = codecs.getreader("utf-16-le")
    assert utf16_le(b'\xff\xfe\x61\x00\x62\x00').read() == 'ab'
    assert utf16_le(b'\xff\xfe\x61\x00\x62\x00', "add_one_codepoint").read() == 'aab'
    assert utf16_le(b'\xff\xfe\x61\x00\x62\x00', "add_utf16_bytes").read() == 'abab'
    assert utf16_le(b'\xff\xfe\x61\x00\x62\x00', "add_utf32_bytes").read() == 'ababcd'
    assert utf16_le(b'\xff\xfe\x61\x00\x62\x00', "strict").read() == 'ab'
    assert utf16_le(b
