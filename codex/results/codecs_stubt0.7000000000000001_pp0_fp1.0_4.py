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

# test different codecs
for encoding in ["utf-8", "utf-16-le", "utf-16-be", "utf-32-le", "utf-32-be"]:

    # test different error handlers
    for error_handler in ["strict", "ignore", "replace", "backslashreplace",
                          "namereplace", "surrogatepass", "surrogateescape",
                          "xmlcharrefreplace", "add_one_codepoint",
                          "add_utf16_bytes", "add_utf32_bytes"]
