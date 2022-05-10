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

def test_idempotent(encoding):
    for i in range(0x10000):
        s = chr(i).encode(encoding, 'surrogateescape')
        s2 = s.decode(encoding, 'surrogateescape').encode(encoding, 'surrogateescape')
        assert s == s2

def test_16b_surrogate_error(encoding):
    s = chr(0xd800).encode(encoding, "surrogateescape")
    assert len(s) == 2
    assert s[0] == 0xdb
    assert (0x40 <= s[1] <= 0xbf) or (0x80 <= s[1] <= 0x9f)
    assert chr(0xd800).encode(encoding, "ignore") == b''
    assert chr(0xd800).encode(encoding, "replace") == b'?\374'
    assert chr(0xd800).encode(encoding, "xmlcharrefreplace") == b'&#55296;'
   
