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
    # test_utf8 
    encoder = codecs.getencoder("utf-8")
    assert encoder("\u3042\ufffd\u3044", "replace") == (b"\xe3\x81\x82\xef\xbf\xbd\xe3\x81\x84", 6)

    encoder = codecs.getencoder("utf-8")
    assert encoder("\u3042\ufffd\u3044", "add_one_codepoint") == (b"\xe3\x81\x82a\xe3\x81\x84", 6)

    # test_utf16 
    encoder = codecs.getencoder("utf-16-le")
    assert encoder("\u3042\ufffd\u3044", "replace") == (b"\x42\x30\xfd\xff\x44\x30", 8)

    encoder = codecs.getencoder("utf-16-le")
    assert encoder("\u3042\
