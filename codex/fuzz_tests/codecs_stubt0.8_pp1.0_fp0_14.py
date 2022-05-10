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

def test_encode(encoding, dec, exc, n=None, nb=None):
    # nb is the number of bytes returned by the error handler
    # n is the number of bytes that should be returned from
    # the call to encode
    if n is None:
        n = len(dec) + (1 if nb is None else nb)
    errors = ["strict", "replace", "ignore", "xmlcharrefreplace",
              "backslashreplace", "namereplace",
              "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]
    for error in errors:
        if error not in ("strict", "replace") and sys.version_info[0] < 3:
            # test only relevant for Python 3
            continue
        try:
            if error in ("add_one_codepoint", "add_utf16_bytes",
                         "add_utf32_bytes"):
                codecs.lookup_error("add_one_codepoint")
            encodefun = codecs.
