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
    # Issue #1514: Encoding with unknown error handler should raise
    # LookupError
    try:
        u"\u3042".encode("euc-jp", "unknown_handler")
    except LookupError:
        pass
    else:
        raise TestFailed("LookupError not raised")

    # Issue #1514: Decoding with unknown error handler should raise
    # LookupError
    try:
        b"\xa1\xa1".decode("euc-jp", "unknown_handler")
    except LookupError:
        pass
    else:
        raise TestFailed("LookupError not raised")

    # Issue #1514: Encoding with invalid error handler should raise
    # TypeError
    try:
        u"\u3042".encode("euc-jp", 42)
    except TypeError:
        pass
    else:
        raise TestFailed("TypeError not raised")

    # Issue #1514: Decoding with invalid error handler should raise
    # TypeError
    try:
       
