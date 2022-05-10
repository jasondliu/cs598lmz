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
    print("Testing UTF-7 codec")
    # Test encoding
    print("Encoding...")
    encoder = "utf-7".encode
    assert encoder("abc") == b"abc"
    assert encoder("abc\u20acdef") == b"abc+AOQ-def"
    assert encoder("+AOQ-def") == b"+AOQ-def"
    assert encoder("+AOQ-de+AN8-") == b"+AOQ-de+AN8-"
    assert encoder("+AOQ-de+AN8-fg") == b"+AOQ-de+AN8-fg"
    assert encoder("+AOQ-de+AN8-fg+AOQ-") == b"+AOQ-de+AN8-fg+AOQ-"
    assert encoder("+AOQ-de+AN8-fg+AOQ-+AN8-") == b"+AOQ-de+AN8-fg+AOQ-+AN8-"
