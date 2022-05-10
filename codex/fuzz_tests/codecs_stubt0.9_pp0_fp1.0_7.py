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

def test_2913():
    # Many UTF-16 variants are possible: big endian, little endian and
    # with or without a Byte Order Mark (BOM). The decoder needs to
    # choose the one fitting the input when no BOM is available
    utf16encoder = codecs.getencoder("utf16")
    utf16decoder = codecs.getdecoder("utf16")
    utf16beencoder = codecs.getencoder("utf-16-be")
    utf16bedecoder = codecs.getdecoder("utf-16-be")
    utf16leencoder = codecs.getencoder("utf-16-le")
    utf16ledecoder = codecs.getdecoder("utf-16-le")
    utf32encoder = codecs.getencoder("utf32")
    utf32decoder = codecs.getdecoder("utf32")
    utf32beencoder = codecs.getencoder("utf-32-be")
    utf32bedecoder = codecs.
