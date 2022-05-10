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
    # UTF-16 decoder
    utf16_decoder = codecs.getincrementaldecoder("utf-16")()
    utf16_decoder.set_error_handler("add_one_codepoint")
    for bytes, string in [
        (b"FF", "a"),
        (b"FFFE", "a"),
        (b"FFFEabc", "abc"),
        (b"FFFF", "a"),
        (b"FFFEFFFE", "a"),
        (b"FFFEFFFF", "a"),
        (b"FFFEabcd", "abcd"),
        (b"FEFFFF", "a"),
        (b"FEFFFEa", "a"),
        (b"FEFFFE", "a"),
        (b"FEFF", "a"),
        (b"0000FEFF", "a"),
        (b"0000FF", "a"),
        (b"0000FE", "a"),
        (b"0000", "a"),
        (b"00FF00FF
