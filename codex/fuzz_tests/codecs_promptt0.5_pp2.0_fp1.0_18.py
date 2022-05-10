import codecs
# Test codecs.register_error()
def handler(exc):
    return (u"\ufffd", exc.end)
codecs.register_error("test.replace", handler)

def test_main():
    assert codecs.lookup_error("test.replace") is handler
    assert codecs.lookup_error("test.replace") is handler
    for encoding in [
        "ascii", "latin-1", "iso8859-1", "iso8859-15", "mac-roman",
        "utf-8", "utf-16", "utf-16-le", "utf-16-be",
        "utf-32", "utf-32-le", "utf-32-be",
        "unicode-internal",
        ]:
        try:
            encoder, decoder, reader, writer = codecs.lookup(encoding)
        except LookupError:
            pass
        else:
            test_encoding(encoding, encoder, decoder, reader, writer)

def test_encoding(encoding, encoder, decoder, reader, writer):

