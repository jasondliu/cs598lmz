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
    import test_support

    encoding = "utf-7"

    # encode
    s = "abc"
    for errors in ["strict", "replace", "ignore", "add_one_codepoint",
                   "add_utf16_bytes", "add_utf32_bytes"]:
        try:
            u = s.encode(encoding, errors=errors)
        except UnicodeError as e:
            pass
        else:
            print(errors)
            print(u)
            print(u.decode(encoding))

    # decode
    s = b"abc"
    for errors in ["strict", "replace", "ignore", "add_one_codepoint",
                   "add_utf16_bytes", "add_utf32_bytes"]:
        try:
            u = s.decode(encoding, errors=errors)
        except UnicodeError as e:
            pass
        else:
            print(errors)
            print(u)
            print(u.encode(encoding))


if __name__
