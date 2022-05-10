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
    # Test UTF-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes"):
            for input in (b'\xff', b'\xff\xff', b'\xff\xff\xff',
                          b'\xff\xff\xff\xff'):
                try:
                    codecs.decode(input, enc, errors)
                except UnicodeDecodeError as exc:
                    if errors == "strict":
                        pass
                    elif errors == "ignore":
                        if len(input) % 2 == 1:
                            raise
                    elif errors == "replace":
                        if len(input) % 2 == 1:
                            raise
                        if len(input) > 2:
                            raise
                    elif errors == "add_one_codepoint":
                        if len(input) % 2 == 1:
                            raise
                        if len
