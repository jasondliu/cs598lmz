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

    def test_register_error(self):
        self.assertIn('add_one_codepoint', codecs.error.keys())
        self.assertIn('add_utf16_bytes', codecs.error.keys())
        self.assertIn('add_utf32_bytes', codecs.error.keys())

        # Unicode codecs:
        self.assertEqual(codecs.decode('ab', 'ascii', 'add_one_codepoint'), 'a')
        self.assertEqual(codecs.decode('ab', 'iso8859_1', 'add_one_codepoint'), 'a')
        self.assertEqual(codecs.decode('ab', 'utf-8', 'add_one_codepoint'), 'a')
        self.assertEqual(codecs.encode('a', 'ascii', 'add_one_codepoint'), b'ab')
        self.assertEqual(codecs.encode('a', 'iso
