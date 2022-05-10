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

tests = [
    # test invalid continuation bytes
    (b"\xf1\x80\xbf\xbf", "utf-8", "utf-8", "replace", "surrogatepass", "\ufffd\ufffd\ufffd"),
    (b"\xf1\x80\xbf\xbf", "utf-8", "utf-8", "ignore", "surrogatepass", ""),
    (b"\xf1\x80\xbf\xbf", "utf-8", "utf-8", "xmlcharrefreplace", "surrogatepass", "\ufffd\ufffd\ufffd"),
    (b"\xf1\x80\xbf\xbf", "utf-8", "utf-8", "backslashreplace", "surrogatepass", "\\U0010ffff"),
    (b"\xf1\x80\xbf\xbf", "utf-8", "utf-8", "add_one_codepoint", "surrogatepass", "a"),
    (b"\xf1\x80\xbf\
