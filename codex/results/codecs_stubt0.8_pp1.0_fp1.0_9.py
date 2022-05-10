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

def test_codecs_utf7():
    def roundtrip(input, errors="strict"):
        encoder = codecs.getencoder("utf-7")
        decoder = codecs.getdecoder("utf-7")
        c, bytes = encoder(input, errors)
        assert bytes == len(input)
        return decoder(c, errors)[0]
    assert roundtrip('Hi Mom -\u263A-!') == 'Hi Mom -\u263A-!'
    assert roundtrip('+') == '+'
    assert roundtrip('+-') == '+-'
    assert roundtrip('\\') == '\\'
    assert roundtrip('\\foo') == '\\foo'
    assert roundtrip('\\') == '\\'
    assert roundtrip('\\foo') == '\\foo'
    assert roundtrip('\\') == '\\'
    assert roundtrip('\\foo') == '\\foo'
    assert roundtrip('\\') == '\\'
    assert roundtrip('\\foo') == '\\foo'
    assert roundtrip('\\
