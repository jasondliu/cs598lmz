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
    # Test that the UTF-16 and UTF-32 codecs can decode invalid byte sequences
    # with the "add_utf16_bytes" and "add_utf32_bytes" error handlers.
    #
    # The "add_one_codepoint" error handler is not used, because it would
    # produce a valid UTF-16 or UTF-32 byte sequence.
    #
    # The UTF-16 codecs should decode the invalid byte sequence as if it
    # contained the two bytes "ab".
    #
    # The UTF-32 codecs should decode the invalid byte sequence as if it
    # contained the four bytes "abcd".
    #
    # The UTF-16 and UTF-32 codecs should not decode the invalid byte sequence
    # as if it contained the single byte "a", because that would produce an
    # invalid UTF-16 or UTF-32 byte sequence.
    #
    # The UTF-16 and UTF-32 codecs should not decode the invalid byte sequence
    # as if it contained the single byte "b", because that would produce an
    #
