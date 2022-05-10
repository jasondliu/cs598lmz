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

class CodecsModuleTest(unittest.TestCase):

    def test_encodings(self):
        encodings = [
            "ascii", "latin-1", "utf-8", "utf-16",
            "utf-16-le", "utf-16-be",
            "utf-32", "utf-32-le", "utf-32-be"]
        for enc in encodings:
            try:
                codecs.lookup(enc)
            except LookupError:
                self.fail("%s is not built-in module" % `enc`)

    @unittest.skipUnless(sys.maxunicode >= 0x10000,
                         "narrow unicode builds only support BMP")
    def test_surrogatepass_handler(self):
        self.assertEqual("surrogatepass" in codecs.__dict__, True)
        self.assertEqual(repr(codecs.surrogatepass_handler),
                         "<surrogatepass error handler>")
        self.assertEqual(cod
