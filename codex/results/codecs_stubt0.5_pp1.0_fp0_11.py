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
    test_streamreader()
    test_incrementalencoder()
    test_incrementaldecoder()
    test_streamwriter()
    test_streamreaderwriter()

def test_streamreader():
    # test StreamReader
    r = codecs.getreader("iso8859-1")("\xe4")
    if r.read() != "\xe4":
        raise TestFailed, "reading from streamreader failed"

    r = codecs.getreader("iso8859-1")("\xe4")
    if r.read(1) != "\xe4":
        raise TestFailed, "reading from streamreader failed"

    r = codecs.getreader("iso8859-1")("\xe4")
    if r.read(10) != "\xe4":
        raise TestFailed, "reading from streamreader failed"

    r = codecs.getreader("iso8859-1")("\xe4")
    if r.read(0) != "":
        raise TestFailed, "reading from streamreader failed"


