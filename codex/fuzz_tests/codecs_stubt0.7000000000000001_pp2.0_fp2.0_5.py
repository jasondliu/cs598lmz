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

def check_codec(name, encoding, decoding):
    # XXX - manually insert correct replacement characters here
    encoding = encoding.replace("[?]", "[\\ufffd]")
    decoding = decoding.replace("[?]", "[\\ufffd]")
    # XXX - manually insert correct number of bytes here
    encoding = encoding.replace("[2]", "[2, 2]")
    encoding = encoding.replace("[4]", "[4, 4]")
    s = "abc"
    assert codecs.encode(s, name, "add_one_codepoint") == encoding
    assert codecs.decode(s.encode(name), name, "add_one_codepoint") == decoding
    # XXX - manually insert correct replacement characters here
    encoding = encoding.replace("[\\ufffd]", "[\\udcff]")
    decoding = decoding.replace("[\\ufffd]", "[\\udcff]")
    # XXX - manually insert correct number of bytes here
    encoding = encoding.replace("[2, 2]", "[3, 3]")
    encoding
