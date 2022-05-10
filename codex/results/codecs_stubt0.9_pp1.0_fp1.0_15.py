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

def test_codec_incrementalencoder():
    from codecs import utf_7_encode, utf_7_decode

    x = "abcd"
    y = utf_7_encode(x, 'add_one_codepoint')[0]
    assert len(x) + 1 == len(y)
    assert utf_7_decode(y, 'strict') == ('abcda', 5)

def test_codec_incrementaldecoder():
    from codecs import utf_16_decode
    from struct import pack

    x = pack('>i', 0x41)
    y = utf_16_decode(x, 'add_utf16_bytes', False)[0]
    assert len(x) + 2 == len(y)
    assert y == 'ab'

    x = pack('>I', 0x41)
    y = utf_16_decode(x, 'add_utf32_bytes', True)[0]
    assert len(x) + 4 == len(y)
   
