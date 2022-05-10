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
    # test that codecs.open() doesn't interfere with the sys.stdout encoding
    # and that it doesn't change the encoding of an already open file
    # (see http://bugs.python.org/issue2517)
    try:
        import _testcapi
    except ImportError:
        raise unittest.SkipTest("need _testcapi")

    # _testcapi.code_newempty fails with a TypeError if the argument is not a
    # bytes object. sys.stdout.encoding is a string, so this would fail.
    if sys.stdout.encoding == "ascii":
        raise unittest.SkipTest("encoding is ascii")

    encoding = sys.stdout.encoding
    _testcapi.code_newempty(encoding.encode("ascii"))
    # If this raises ValueError, then the encoding is invalid and we can't
    # test it.
    codecs.lookup(encoding)

    with codecs.open(os.devnull, "w",
