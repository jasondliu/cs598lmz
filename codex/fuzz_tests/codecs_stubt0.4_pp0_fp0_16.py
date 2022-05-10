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
    for encoding in ["utf-8", "utf-16", "utf-32"]:
        for i in range(0, len(encoding)):
            try:
                codecs.decode(encoding[:i], encoding)
            except UnicodeDecodeError as exc:
                if encoding == "utf-8":
                    codecs.decode(encoding[:i], encoding, "add_one_codepoint")
                    codecs.decode(encoding[:i], encoding, "add_utf16_bytes")
                    codecs.decode(encoding[:i], encoding, "add_utf32_bytes")
                elif encoding == "utf-16":
                    codecs.decode(encoding[:i], encoding, "add_one_codepoint")
                    codecs.decode(encoding[:i], encoding, "add_utf16_bytes")
                    try:
                        codecs.decode(encoding[:i], encoding, "add_utf32_bytes")
                    except UnicodeDecodeError as exc:

