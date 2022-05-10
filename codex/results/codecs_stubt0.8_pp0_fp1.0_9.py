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

try:
    unicode('\ud800\ud800', "unicode-escape", "add_one_codepoint")
except:
    print("exception raised, that's OK") # Should raise an exception

class Test(unittest.TestCase):
    def test_utf16_surrogates(self):
        self.assertEqual(unicode('\ud800\ud800', "unicode-escape", "add_one_codepoint"), "\ud800a")
        self.assertEqual(unicode('\ud800\ud800', "unicode-escape", "add_utf16_bytes"), "\ud800a")
        self.assertEqual(unicode('\ud800\ud800', "unicode-escape", "add_utf32_bytes"), "\ud800a")
        self.assertEqual(unicode('\ud800\ud800', "raw-unicode-escape", "add_utf16_bytes"), "\ud800\ud800")
        self.assertEqual(unicode('\ud800\ud800', "utf-16", "add
