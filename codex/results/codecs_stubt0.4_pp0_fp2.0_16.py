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

class TestCodecs(unittest.TestCase):

    def test_bug_834630(self):
        # bug 834630:  codecs.charmap_encode() didn't raise a
        # UnicodeEncodeError with a reason when a character mapping
        # wasn't found
        self.assertRaises(UnicodeEncodeError,
                          codecs.charmap_encode, "abc", "strict",
                          {ord("a"): None})

    def test_bug_834817(self):
        # bug 834817:  codecs.charmap_encode() didn't raise a
        # UnicodeEncodeError when a character mapping was found to be
        # None
        self.assertRaises(UnicodeEncodeError,
                          codecs.charmap_encode, "abc", "strict",
                          {ord("a"): None})

    def test_bug_834831(self):
        # bug 834831:  codecs.charmap_encode() didn't raise a

