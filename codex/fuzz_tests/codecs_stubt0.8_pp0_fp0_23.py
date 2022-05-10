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

class TestUnicodeDecode(unittest.TestCase):

    def test_decoding_errors(self):
        for encoding in ("utf-8", "utf-16", "utf-32",
                         "utf-8-sig", "utf-16-le", "utf-16-be",
                         "utf-32-le", "utf-32-be"):
            with self.subTest(encoding=encoding):
                self.check_decoding_errors(encoding)

    def check_decoding_errors(self, encoding):
        errors = ["strict", "ignore", "replace",
                  "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"
                 ]
        if encoding in ("utf-16", "utf-32", "utf-16-le", "utf-32-le"):
            errors += ["surrogatepass"]
        if encoding in ("utf-16-le", "utf-16-be",
                        "utf-32-le", "utf-32-be"):
            errors
