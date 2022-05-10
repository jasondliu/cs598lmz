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

# test codecs.decode()

def test_decode():
    # test decoding of surrogate pairs
    assert codecs.decode("\ud800\udc00", "utf-16") == "\U00010000"
    assert codecs.decode("\ud800\udc00", "utf-16-be") == "\U00010000"
    assert codecs.decode("\ud800\udc00", "utf-16-le") == "\U00010000"
    assert codecs.decode("\ud800\udc00", "utf-32") == "\U00010000"
    assert codecs.decode("\ud800\udc00", "utf-32-be") == "\U00010000"
    assert codecs.decode("\ud800\udc00", "utf-32-le") == "\U00010000"
    assert codecs.decode(b"\x00\x01\x00\x00\x00\x00\x00\x00", "utf-32-be") == "\U00000001"
    assert codec
