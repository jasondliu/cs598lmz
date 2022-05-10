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
    # Test the "add_one_codepoint" codec
    for encoding in ('ascii', 'utf-8', 'utf-16', 'utf-32'):
        decoder = codecs.getdecoder(encoding)
        encoder = codecs.getencoder(encoding)
        for input, expected in (
            (b'\x80', 'a\ufffd'),
            (b'\x80\x80', 'a\ufffd\ufffd'),
            (b'\x80\x80\x80', 'a\ufffd\ufffd\ufffd'),
            (b'\x80\x80\x80\x80', 'a\ufffd\ufffd\ufffd\ufffd'),
        ):
            # Test decoding
            output, consumed = decoder(input, "add_one_codepoint")
            assert output == expected
            assert consumed == len(input)
            # Test encoding
            output, consumed = encoder(expected, "add_one_codepoint")
            assert output ==
