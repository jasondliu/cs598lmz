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

def test_decode_error(decoder, input, output, errors):
    assert decoder(input, errors) == (output, len(input))
    assert decoder(input, errors, True) == (output, len(input), 1)

def test_encode_error(encoder, input, output, errors):
    assert encoder(input, errors) == (output, len(input))
    assert encoder(input, errors, True) == (output, len(input), 1)

def test_decode(decoder, input, output):
    assert decoder(input) == (output, len(input))
    assert decoder(input, True) == (output, len(input), 1)

def test_encode(encoder, input, output):
    assert encoder(input) == (output, len(input))
    assert encoder(input, True) == (output, len(input), 1)

def test_decode_encode(decoder, encoder, input, output):
    assert decoder(encoder(input)[0]) ==
