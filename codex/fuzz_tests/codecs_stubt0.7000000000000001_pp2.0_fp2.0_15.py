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

errors = ['strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes', 'surrogateescape', 'surrogatepass']

def get_decoder(encoding):
    return codecs.getincrementaldecoder(encoding)

def get_encoder(encoding):
    return codecs.getincrementalencoder(encoding)

def check_decoder_state(decoder):
    if hasattr(decoder, 'buffer'):
        return len(decoder.buffer)
    else:
        return 0

def check_encoder_state(encoder):
    if hasattr(encoder, 'buffer'):
        return len(encoder.buffer)
    else:
        return 0

def test_errors(decoder, encoder, encoding, errors=errors):
    for error in errors:
        try:
            d = decoder(error=error)
            e = encoder(error=error)
        except LookupError:
            continue


