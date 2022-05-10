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

# utf-8
utf8 = codecs.getencoder("utf-8")
utf8dec = codecs.getdecoder("utf-8")

# utf-16
utf16 = codecs.getencoder("utf-16")
utf16dec = codecs.getdecoder("utf-16")

# utf-32
utf32 = codecs.getencoder("utf-32")
utf32dec = codecs.getdecoder("utf-32")

# utf-32-le
utf32le = codecs.getencoder("utf-32-le")
utf32ledec = codecs.getdecoder("utf-32-le")

# utf-32-be
utf32be = codecs.getencoder("utf-32-be")
utf32bedec = codecs.getdecoder("utf-32-be")

# utf-16-le
utf16le = codecs.getencoder("utf-16-le")
utf16ledec = codecs.getdecoder("utf-16-le")

#
