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

def test_add_one_codepoint(test_decode, codec_name):
    assert test_decode(b'\xff',
                       codec_name, 'add_one_codepoint') == (u'a', 1)

def test_add_utf16_bytes(test_decode, codec_name):
    if codec_name == "utf-16":
        assert test_decode(b'\xff',
                           codec_name, 'add_utf16_bytes') == (u'ab', 2)
    else:
        with pytest.raises(UnicodeDecodeError) as excinfo:
            test_decode(b'\xff',
                        codec_name, 'add_utf16_bytes')
        assert excinfo.value.start == 0

def test_add_utf32_bytes(test_decode, codec_name):
    if codec_name == "utf-32":
        assert test_decode(b'\xff',
                           codec_name, 'add_utf32_bytes') == (u'abcd
