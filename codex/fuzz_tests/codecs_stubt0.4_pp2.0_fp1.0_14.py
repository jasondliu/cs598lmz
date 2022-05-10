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
    # Testing UTF-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        for bom in (b'', b'\xff\xfe', b'\xfe\xff'):
            for err in (None, "strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes"):
                for s in (b'\xff', b'\xff\xff', b'\xff\xff\xff', b'\xff\xff\xff\xff'):
                    for i in range(len(s)):
                        if err == "add_utf16_bytes":
                            # This is a special case: the error handler
                            # adds bytes, but it adds them at the start
                            # of the input, not at the current position.
                            # This means that the error handler is called
                            # only once, and that the bytes it adds are
                            # ignored.
                            with self.assertRaises(UnicodeDecodeError)
