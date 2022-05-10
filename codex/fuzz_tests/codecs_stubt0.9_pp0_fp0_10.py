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

class TestDecoding(unittest.TestCase):

    def test_hindi(self):
        # devanagari vowel sign i, followed by a devanagari aspa
        # takes two bytes, whereas the aspa alone encodes in one byte
        s = 'िँ'
        expected = '\u093f\u0901'
        self.assertEqual(expected.encode('utf-8').decode('utf-8', 'strict'), expected)
        self.assertEqual(s.encode('utf-8').decode('utf-8', 'strict'), expected)

        self.assertEqual(expected.encode('utf-8').decode('utf-8', 'ignore'), expected)
        self.assertEqual(s.encode('utf-8').decode('utf-8', 'ignore'), 'ि')

        self.assertEqual(expected.encode('utf-8').decode('utf-8', 'replace'), expected)
        self.assertEqual(s.encode('utf-8').decode
