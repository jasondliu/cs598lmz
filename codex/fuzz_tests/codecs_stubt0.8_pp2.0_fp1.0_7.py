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
    try:
        b"abcabcabcabcabcabcabcabcabcabc\xa0\xa0\xa0".decode("utf8", "add_one_codepoint")
    except Exception as e:
        if "utf8" != e.encoding:
            raise Exception("Expect encoding utf8, got: %s" % e.encoding)
        if e.reason != "add_one_codepoint":
            raise Exception("Expect reason add_one_codepoint, got: %s" % e.reason)
        if e.object is not None:
            raise Exception("Expect object to be None, got %s" % e.object)
        if not isinstance(e.start, int) or e.start < 0:
            raise Exception("Expect start to be a zero or positive integer, got: %s" % e.start)

    try:
        b"abcabcabcabcabcabcabcabcabcabc\xa0\xa0\xa0".decode("utf8", "add_utf16_bytes")

