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

# UTF-8

def test_utf8_decode_error_handling(codec_name):
    # Issue #24401: UTF-8 decoder should not accept surrogate characters
    # as valid UTF-8 bytes.
    for surrogate in (0xD800, 0xDFFF):
        for c in (surrogate,
                  surrogate.to_bytes(2, 'big'),
                  surrogate.to_bytes(4, 'big')):
            for errors in ('strict', 'ignore', 'replace', 'surrogateescape',
                           'surrogatepass', 'add_one_codepoint'):
                with pytest.raises(UnicodeDecodeError):
                    c.decode(codec_name, errors)
            with pytest.raises(UnicodeDecodeError):
                c.decode(codec_name, 'add_utf16_bytes')
            with pytest.raises(UnicodeDecodeError):
                c.decode(codec_name, 'add_utf32_bytes')

def test
