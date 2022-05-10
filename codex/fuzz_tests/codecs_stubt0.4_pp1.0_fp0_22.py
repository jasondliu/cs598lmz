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
    # This test is a bit of a hack, as it requires the UTF-16 and UTF-32
    # codecs to be available.  If they aren't, we just skip the test.
    try:
        codecs.lookup("utf-16")
    except LookupError:
        raise unittest.SkipTest("UTF-16 codec not available")
    try:
        codecs.lookup("utf-32")
    except LookupError:
        raise unittest.SkipTest("UTF-32 codec not available")

    # Test that the surrogatepass error handler skips over unpaired
    # surrogates.
    for encoding in ("utf-16", "utf-32"):
        for error_handler in ("surrogatepass", "add_one_codepoint",
                              "add_utf16_bytes", "add_utf32_bytes"):
            for surrogate in (0xd800, 0xdc00):
                for byte in (0xff, 0xfe):
                    for byteorder in ('little', 'big'):
                        byteorder
