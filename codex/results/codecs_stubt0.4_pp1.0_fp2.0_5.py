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

    def test_bug_834630(self):
        # bug 834630 reported by Just van Rossum:  UTF-7 output uses
        # surrogates for characters > 0xffff
        s = 'A\U000abcde'
        for errors in ('strict', 'replace', 'ignore'):
            for encoding in ('utf-7', 'utf-8', 'utf-16', 'utf-32'):
                self.assertEqual(s.encode(encoding, errors),
                                 s.encode(encoding, 'surrogateescape').decode(encoding, errors))

    def test_bug_834696(self):
        # bug 834696 reported by Just van Rossum:  UTF-7 decoder ignores
        # illegal continuation bytes
        for encoding in ('utf-7', 'utf-8', 'utf-16', 'utf-32'):
            self.assertRaises(UnicodeDecodeError, b'\xff'.decode, encoding)

    def test_bug_8
