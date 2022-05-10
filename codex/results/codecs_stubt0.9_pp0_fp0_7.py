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


def reset():
    for encode in "utf-16", "utf-16be":
        for error in ("strict", "ignore", 
                      "replace", "add_one_codepoint", 
                      "surrogateescape", "surrogatepass"):
            codecs.register_error(error, None)

buf = [("abcd", "utf-8", "strict", "utf-8"),
       ("abcd", "utf-8", "ignore", "utf-8"),
       ("abcd", "utf-8", "replace", "utf-8"),
       ("abcd", "utf-8", "surrogateescape", "utf-8"),
       ("abcd", "utf-8", "surrogatepass", "utf-8"),
       ("abcd", "utf-8", "add_one_codepoint", "utf-8"),
       ("abcd", "utf-8", "add_utf16_bytes", "utf-16"),
       ("abcd", "utf-8", "add_utf32_bytes", "utf-32"),
