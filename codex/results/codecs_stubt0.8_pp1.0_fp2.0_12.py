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

class CodecsModTest(unittest.TestCase):

    def test_register_error(self):
        s = "\xff"
        for errors in ("ignore", "replace", "add_one_codepoint"):
            self.assertEqual(
                    codecs.utf_8_decode(s, errors)[0],
                    "\uFFFD" if errors == "replace" else "a",
                    )
        s = b"\xff\xff"
        for errors in ("ignore", "replace", "add_utf16_bytes"):
            self.assertEqual(
                    codecs.utf_16_le_decode(s, errors)[0],
                    "\uFFFD" if errors == "replace" else "a",
                    )
        s = b"\xff\xff\xff\xff"
        for errors in ("ignore", "replace", "add_utf32_bytes"):
            self.assertEqual(
                    codecs.utf_32_le_decode(s, errors)[0],
                    "\uFFFD" if errors == "replace"
