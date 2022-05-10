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

class Test_Unicode(unittest.TestCase):

    def test_add_one_codepoint(self):
        self.assertEqual(codecs.decode("\xff", "utf-8", "add_one_codepoint"), "a")

    def test_add_utf16_bytes(self):
        self.assertEqual(codecs.decode("\xff", "utf-16", "add_utf16_bytes"), "a")

    def test_add_utf32_bytes(self):
        self.assertEqual(codecs.decode("\xff", "utf-32", "add_utf32_bytes"), "a")


if __name__ == "__main__":
    unittest.main()
