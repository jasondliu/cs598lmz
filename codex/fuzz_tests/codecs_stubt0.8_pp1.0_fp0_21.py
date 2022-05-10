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

def test_utf16_errors(self):
    self.check_error("utf16", "strict", b"\x00\x61\x00\x00", 2,
                     "utf-16-be", 2, "surrogates not allowed")
    self.check_error("utf-16-le", "strict", b"\x61\x00\x00\x00", 2,
                     "utf-16-le", 2, "surrogates not allowed")
    self.check_error("utf-16-be", "ignore", b"\x00\x61\x00\x00", 1,
                     "utf-16-be", 2, "surrogates not allowed")
    self.check_error("utf-16-le", "ignore", b"\x61\x00\x00\x00", 1,
                     "utf-16-le", 2, "surrogates not allowed")
    self.check_error("utf-16-be", "replace", b"\x00\x61\x00\x00", 1,
                    
