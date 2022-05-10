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
    # Test for issue #8786: UTF-16 and UTF-32 codecs should use
    # surrogatepass error handler when surrogateescape is not available
    for encoding in "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be":
        with support.check_warnings((
            "can't decode byte 0xff in position 0: truncated data",
            "can't decode byte 0xff in position 1: truncated data",
            "can't decode byte 0xff in position 2: truncated data",
            "can't decode byte 0xff in position 3: truncated data",
            "can't decode byte 0xff in position 4: truncated data",
            "can't decode byte 0xff in position 5: truncated data",
            "can't decode byte 0xff in position 6: truncated data",
            "can't decode byte 0xff in position 7: truncated data",
            "can't decode byte 0xff in position 8: truncated data",
            "can't decode byte 0
