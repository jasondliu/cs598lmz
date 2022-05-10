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

def test_surrogatepass():
    assert codecs.decode("\ud800\ud800", "surrogatepass") == "\ud800\ud800"
    assert codecs.decode("\ud800\ud800\ud800", "surrogatepass") == "\ud800\ud800\ud800"
    assert codecs.decode("\ud800\ud800\ud800", "surrogatepass", "surrogatepass") == "\ud800\ud800\ud800"
    raises(UnicodeDecodeError, codecs.decode, "\ud800\ud800\ud800", "surrogatepass", "replace")
    assert codecs.decode("\ud800\ud800\ud800", "surrogatepass", "ignore") == "\ud800"
    assert codecs.decode("\ud800\ud800\ud800", "surrogatepass", "add_one_codepoint") == "aa\ud800"
    assert codecs.decode("\ud800\ud800\ud800", "surrogatepass", "add
