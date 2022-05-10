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

def test_utf16_errors(encoding):
    encoder = codecs.getencoder(encoding)
    decoder = codecs.getdecoder(encoding)
    for errors in ["ignore", "replace", "add_one_codepoint", "add_utf16_bytes"]:
        assert encoder("\u0385\u0385", errors=errors) == (b'\xdd\x85\xdd\x85', 4)
        assert decoder(b'\xdd\x85\xdd\x85', errors=errors) == ("\u0385\u0385", 4)
        assert encoder("\u0385\u0385\u0385", errors=errors) == (b'\xdd\x85\xdd\x85\xdd\x85', 6)
        assert decoder(b'\xdd\x85\xdd\x85\xdd\x85', errors=errors) == ("\u0385\u0385\u0385", 6)

def test_utf32_errors(enc
