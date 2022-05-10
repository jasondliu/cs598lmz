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

compare_output("utf-16-le", "utf-16-le",
               b"",
               b"",
               [("ignore", b''),
                ("replace", b'?'),
                ("xmlcharrefreplace", b'&#65533;'),
                ("backslashreplace", b'\\udcff'),
                ("namereplace", b'\\udcff'),
                ("add_one_codepoint", b'a'),
                ("add_utf16_bytes", b'\xff\xfea\0b\0'),
                ("add_utf32_bytes", b'\xff\xfe\0\0a\0\0\0b\0\0\0c\0\0\0d\0\0\0')])
compare_output("utf-16-le", "utf-16-le",
               b"test",
               b"test",
               [("ignore", b'test'),
                ("replace", b'test'),
                ("xmlcharrefreplace", b'test'),
                ("backslashreplace", b'test
