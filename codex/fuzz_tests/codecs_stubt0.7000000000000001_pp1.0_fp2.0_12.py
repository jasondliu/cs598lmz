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

# bytes to unicode

for enc in "utf-8", "utf-16-le", "utf-16-be", "utf-32-le", "utf-32-be":
    for error in "strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes":
        assert codecs.decode("abc", enc, error) == "abc"
        assert codecs.decode("\xff", enc, error) == "\ufffd"
        assert codecs.decode("\xff\xff", enc, error) == "\ufffd\ufffd"
        assert codecs.decode("\xff\xff\xff", enc, error) == "\ufffd\ufffd\ufffd"
        assert codecs.decode("\xff\xff\xff\xff", enc, error) == "\ufffd\ufffd\ufffd\ufffd"
        assert codecs.decode("\xff\xff\xff\xff\xff", enc, error) == "\ufffd\ufffd\ufffd\ufffd\ufffd"
        assert codec
