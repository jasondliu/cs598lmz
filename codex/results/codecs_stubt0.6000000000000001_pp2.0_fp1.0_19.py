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

def test_decode(encoding, data, add_bytes, error_handler):
    dec = codecs.getdecoder(encoding)
    data = bytes(data)
    result = dec(data, error_handler)[0]
    error_handler = codecs.lookup_error(error_handler)
    handler_result = error_handler(UnicodeDecodeError(encoding, data, 0, 1, "ouch"))[0]
    assert result == handler_result

def test_encode(encoding, data, add_bytes, error_handler):
    data = "".join(chr(i) for i in data)
    enc = codecs.getencoder(encoding)
    result = enc(data, error_handler)[0]
    error_handler = codecs.lookup_error(error_handler)
    handler_result = error_handler(UnicodeEncodeError(encoding, data, 0, 1, "ouch"))[0]
    assert result == handler_result

def test_decode_utf8():
    yield test
