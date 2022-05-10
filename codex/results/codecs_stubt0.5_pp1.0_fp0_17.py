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
    # Issue #9497: UTF-16 decoder should raise a ValueError when the input
    # contains an odd number of bytes.
    for decoder in ["utf-16-be", "utf-16-le"]:
        try:
            codecs.getdecoder(decoder)(b'\xff')
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError not raised")

    # Issue #9498: UTF-32 decoder should raise a ValueError when the input
    # contains an odd number of bytes.
    for decoder in ["utf-32-be", "utf-32-le"]:
        try:
            codecs.getdecoder(decoder)(b'\xff')
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError not raised")

    # Issue #9499: UTF-16 decoder should raise a ValueError when the input
    # contains an odd number of bytes.
    for decoder in ["utf-16-be", "utf-16-le
