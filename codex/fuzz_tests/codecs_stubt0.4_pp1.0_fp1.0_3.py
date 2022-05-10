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
    # UTF-8
    encoder = codecs.getincrementalencoder("utf-8")()
    assert encoder.encode("\u3042") == b'\xe3\x81\x82'
    assert encoder.encode("\u3042", "add_one_codepoint") == b'\xe3\x81\x82a'
    assert encoder.encode("\u3042", "add_utf16_bytes") == b'\xe3\x81\x82ab'
    assert encoder.encode("\u3042", "add_utf32_bytes") == b'\xe3\x81\x82abcd'

    # UTF-16
    encoder = codecs.getincrementalencoder("utf-16")()
    assert encoder.encode("\u3042") == b'\xff\xfeB\x04'
    assert encoder.encode("\u3042", "add_one_codepoint") == b'\xff\xfeB\x
