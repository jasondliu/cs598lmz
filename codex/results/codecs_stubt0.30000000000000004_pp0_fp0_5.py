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
    # Test decoding with errors
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input in ("\xff", "\xff\xff", "\xff\xff\xff\xff"):
                if encoding == "utf-8" and errors == "add_utf16_bytes":
                    # This is not supported, but we don't want to crash
                    continue
                if encoding == "utf-16" and errors == "add_utf32_bytes":
                    # This is not supported, but we don't want to crash
                    continue
                if encoding == "utf-32" and errors == "add_utf16_bytes":
                    # This is not supported, but we don't want to crash
                    continue
                print(encoding, errors, input)
                u = input.decode(encoding, errors)
                print(u)
                b = u
