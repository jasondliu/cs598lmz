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
    # Test that the codecs module implements the API specified in PEP 100.
    # This test is not exhaustive, but it should catch some errors.

    # Test the open() API
    f = codecs.open("test.txt", "w", "latin-1")
    f.write("abc")
    f.close()
    f = codecs.open("test.txt", "r", "latin-1")
    if f.read() != "abc":
        raise TestFailed("reading from latin-1 encoded file failed")
    f.close()
    os.unlink("test.txt")

    # Test the EncodedFile API
    f = codecs.open("test.txt", "w", "utf-16")
    f.write("abc")
    f.close()
    f = codecs.open("test.txt", "r", "utf-16")
    if f.read() != "abc":
        raise TestFailed("reading from utf-16 encoded file failed")
    f.close()
    os.
