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
    # test utf-16-le
    utf16_le_decoder = codecs.getdecoder("utf-16-le")
    utf16_le_encoder = codecs.getencoder("utf-16-le")
    utf16_le_encoder(u"\u1234\u5678", "add_one_codepoint")
    utf16_le_encoder(u"\u1234\u5678", "add_utf16_bytes")
    utf16_le_decoder(b'\x34\x12\x78\x56', "add_one_codepoint")
    utf16_le_decoder(b'\x34\x12\x78\x56', "add_utf16_bytes")

    # test utf-16-be
    utf16_be_decoder = codecs.getdecoder("utf-16-be")
    utf16_be_encoder = codecs.getencoder("utf-16-be")
   
