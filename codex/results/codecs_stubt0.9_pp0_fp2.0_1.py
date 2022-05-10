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

def main():
    import codecs
    codecs.register_error("add_one_codepoint", add_one_codepoint)
    codecs.register_error("add_utf16_bytes", add_utf16_bytes)
    codecs.register_error("add_utf32_bytes", add_utf32_bytes)

    uc = "\u00DF"
    print(uc)
    print(uc.encode("ascii", "replace").decode("ascii", "replace"))
    print(uc.encode("utf8", "replace"))
    print(uc.encode("utf8", "replace").decode("ascii", "replace"))
    print(uc.encode("utf8", "replace").decode("utf8", "ignore"))
    print(uc.encode("utf8", "replace").decode("utf8", "strict"))

    uc = "\u71ff"
    print(uc)
    print(uc.encode("iso-8859-1", "replace"))
    print(uc.encode
