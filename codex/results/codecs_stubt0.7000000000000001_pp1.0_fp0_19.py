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

# XXX more tests are needed for the various signatures

def test_bad_args():
    for codec in "utf_7 utf_8_sig utf_16 utf_16_be utf_16_le utf_32 utf_32_be utf_32_le".split():
        f = codecs.getincrementalencoder(codec)
        raises(TypeError, f)
        raises(TypeError, f, False)
        raises(TypeError, f, "utf-8")
    for codec in "utf_16 utf_16_be utf_16_le utf_32 utf_32_be utf_32_le".split():
        f = codecs.getincrementaldecoder(codec)
        raises(TypeError, f)
        raises(TypeError, f, False)
        raises(TypeError, f, "utf-8")

def test_utf8():
    f = codecs.getincrementalencoder("utf8")()
    raises(UnicodeDecodeError, f.decode, b
