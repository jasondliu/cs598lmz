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

for errors in ("strict",
               "ignore",
               "replace",
               "xmlcharrefreplace",
               "backslashreplace",
               "namereplace",
               "add_one_codepoint",
               "add_utf16_bytes",
               "add_utf32_bytes",
               "surrogateescape"):
    for encoding in ("ascii", "utf-8", "utf-16", "utf-32", "iso2022_jp"):
        codec = "{0}_{1}".format(encoding, errors)
        try:
            print("\ntry {0}:".format(codec))
            codecs.lookup(codec)
            print("found: {0}".format(codec))
        except LookupError as e:
            print("unknown encoding: {0}".format(e))
            continue

        # each test case is list of two items: input string and expected
        # result string
        test_cases = (
        # \uDCFF is an illegal codepoint
        ("\uDCFF"),

