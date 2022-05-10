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
    # Test error handling
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input in (b'\xff', b'\xff\xff', b'\xff\xff\xff\xff'):
                for i in range(1, len(input)):
                    # Test partial decoding
                    decoder = codecs.getincrementaldecoder(encoding)()
                    decoder.setstate(0)
                    try:
                        decoder.decode(input[:i], errors)
                    except UnicodeDecodeError as exc:
                        pass
                    else:
                        raise AssertionError("expected UnicodeDecodeError")
                    decoder.decode(input[i:], errors)
                    try:
                        decoder.decode("", errors)
                    except UnicodeDecodeError as exc:
                        pass
                    else:
                       
