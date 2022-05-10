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
    # Test UTF-8 decoding
    for i in range(0xD800, 0xE000):
        if i not in (0xD800, 0xDFFF):
            # test all illegal codepoints except surrogates
            s = bytes([i])
            try:
                s.decode("utf-8")
            except UnicodeDecodeError as exc:
                if exc.object is not s:
                    raise Exception("wrong exception object")
                if exc.start != 0:
                    raise Exception("wrong exception start")
                if exc.end != 1:
                    raise Exception("wrong exception end")
                if exc.reason != "illegal UTF-8 sequence":
                    raise Exception("wrong exception reason")
                if exc.object[exc.start:exc.end] != s:
                    raise Exception("wrong exception object slice")
            else:
                raise Exception("UnicodeDecodeError not raised")

    # Test UTF-8 decoding with errors='ignore'
    for i in range(0xD800, 0xE000):
        if i not
