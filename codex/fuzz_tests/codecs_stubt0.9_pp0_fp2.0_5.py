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

class CodecsBackportTest(unittest.TestCase):
    def test_mbcs_encode(self):
        encoded = codecs.mbcs_encode(u'\u0085aéé')
        if sys.platform == "win32":
            assert len(encoded) == 5
        else:
            assert len(encoded) == 7

        encoded = codecs.mbcs_encode(u'\u0185aéé', "replace")
        if sys.platform == "win32":
            assert len(encoded) == 5
        else:
            assert len(encoded) == 7

    def test_mbcs_decode(self):
        if sys.platform == "win32":
            decoded = codecs.mbcs_decode(b"a\xFC\xEA\xFF\xFC")
            assert len(decoded) == 4
            assert decoded == (u'a\u00FC\u00EA\uFFFD', 4)
        else:
            decoded = codecs.mbcs_decode(
