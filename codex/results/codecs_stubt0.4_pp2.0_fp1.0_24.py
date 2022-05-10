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
    # This test is not run automatically, because it requires a
    # non-compliant UTF-16 codec.
    import _codecs_cn, _testcapi
    if not hasattr(_codecs_cn, 'utf_16_decode'):
        raise unittest.SkipTest("need a non-compliant UTF-16 codec")

    # Test UTF-16 codec
    utf16 = codecs.getencoder("utf-16")
    utf16_dec = codecs.getdecoder("utf-16")
    utf16le = codecs.getencoder("utf-16-le")
    utf16le_dec = codecs.getdecoder("utf-16-le")
    utf16be = codecs.getencoder("utf-16-be")
    utf16be_dec = codecs.getdecoder("utf-16-be")

    # Test basic functionality
    for encoder, decoder in [
        (utf16, utf16_dec),
        (utf16le, utf
