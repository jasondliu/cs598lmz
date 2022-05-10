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

def is_utf_variant(encoding):
    return encoding.startswith("utf-")

class UnicodeEncodeErrorTests(unittest.TestCase):
    def test_encode(self):
        # Testing UnicodeEncodeError encoding
        u = chr(sys.maxunicode)
        for encoding in ("ascii", "latin-1", "utf-8", "utf-16", "utf-32"):
            for errors in ("strict", "replace", "ignore", "backslashreplace",
                           "xmlcharrefreplace", "surrogateescape",
                           "surrogatepass", "namereplace"):
                try:
                    u.encode(encoding, errors)
                except UnicodeEncodeError as exc:
                    self.assertEqual(exc.encoding, encoding)
                    self.assertEqual(exc.object, u)
                    self.assertEqual(exc.end, 1)
                    self.assertEqual(type(exc.end), int)
                    self.assertEqual(exc.start, 0)
