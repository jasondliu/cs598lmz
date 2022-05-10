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

# test codecs.register_error
def test_codecs_register_error():
    codecs.register_error("test", lambda exc: ("", exc.start + 1))

    assert codecs.lookup_error("test") is not None

def test_utf16_decode():
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x01\x00\x2a') == ('\u0001*', 4)
    assert codecs.utf_16_decode(b'\x00\x01\x00\x2a', byteorder='little') == ('\u0001*', 4)
    assert codecs.utf_16_decode(b'\x00\x01\x00\x2a', byteorder='big') == ('\u0100*', 4)
    assert codecs.utf_16_decode(b'\xff\xfe\x00\x01\x00\x2a', errors='strict') == ('\u0001*', 4)
    # invalid bytes
   
