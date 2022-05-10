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

class UnicodeDecodeTest(unittest.TestCase):
    def assertDecodes(self, input, errors, output):
        self.assertEqual(input.decode("ascii", errors), output)
        self.assertEqual(codecs.decode(input, "ascii", errors), output)
        self.assertEqual(input.decode("latin-1", errors), output)
        self.assertEqual(codecs.decode(input, "latin-1", errors), output)

    def assertDecodesToSyntaxError(self, input):
        self.assertRaises(SyntaxError, input.decode, "ascii", "surrogateescape")
        self.assertRaises(SyntaxError, input.decode, "latin-1", "surrogateescape")
        self.assertRaises(SyntaxError, input.decode, "ascii", "surrogatepass")
        self.assertRaises(SyntaxError, input.decode, "latin-1", "surrogatepass")
