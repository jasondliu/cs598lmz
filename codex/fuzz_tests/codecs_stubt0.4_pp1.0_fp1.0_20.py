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

# UTF-8

def test_utf8_replace():
    assert codecs.decode("\xff", "utf-8", "replace") == "\ufffd"
    assert codecs.decode("\xff", "utf-8", "backslashreplace") == "\\xff"
    assert codecs.decode("\xff", "utf-8", "xmlcharrefreplace") == "&#xff;"
    assert codecs.decode("\xff", "utf-8", "namereplace") == "\\ufffd"
    assert codecs.decode("\xff", "utf-8", "surrogateescape") == "\udcff"
    assert codecs.decode("\xff", "utf-8", "surrogatepass") == "\udcff"
    assert codecs.decode("\xff", "utf-8", "ignore") == ""
    assert codecs.decode("\xff", "utf-8", "add_one_codepoint") == "a"
    assert codecs.decode("\xff", "utf-8", "add_
