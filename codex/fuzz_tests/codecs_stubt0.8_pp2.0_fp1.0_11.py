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
    import re
    import unicodedata
    for encoding in ("latin-1", "utf-8", "utf-16-be", "utf-32"):
        print("Testing %s" % encoding)
        encoder = codecs.getencoder(encoding)
        decoder = codecs.getdecoder(encoding)
        # Surrogate characters should be decoded as individual codepoints
        # in UTF-16 and UTF-32
        if encoding in ("utf-16-be", "utf-32"):
            assert decoder(b'\x00\xd8\x00\xdc', "surrogatepass") == \
                (u'\U00010330', 4)
            assert decoder(b'\x00\xd8\x00\xdc\x00\x00', "surrogatepass") == \
                (u'\U00010330\u0000', 6)
        else:
            assert decoder(b'\x00\xd8\x00\xdc', "surrogate
