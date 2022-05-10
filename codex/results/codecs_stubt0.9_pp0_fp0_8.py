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

text = u"abcde"

def check_decode(decoder):
    real, bytes_in = decoder.decode(text.encode("utf-8"),
                                    "backslashreplace",
                                    "add_one_codepoint")
    assert len(real) == len(text)*2
    assert real.startswith(text)
    assert len(real) == len(bytes_in)

    real, bytes_in = decoder.decode(text.encode("utf-16"),
                                    "backslashreplace",
                                    "add_utf16_bytes")
    assert len(real) == len(text)*2
    assert real.startswith(text)
    assert len(real) == len(bytes_in)

    real, bytes_in = decoder.decode(text.encode("utf-32"),
                                    "backslashreplace",
                                    "add_utf32_bytes")
    assert len(real) == len(text)*2
    assert real.startswith(text)
    assert len(
