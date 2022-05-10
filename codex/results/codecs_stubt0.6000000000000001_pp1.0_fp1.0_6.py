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

class TestUTF7(unittest.TestCase):
    def test_partial(self):
        # regression test for http://bugs.python.org/issue17559
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode, b'+',
                          errors='strict', final=True)

    def test_utf7_encode(self):
        self.assertEqual(codecs.utf_7_encode(b'\x80'), (b'+AOAA-', 5))
        self.assertEqual(codecs.utf_7_encode(b'\xff'), (b'+//8-', 5))
        self.assertEqual(codecs.utf_7_encode(b'\u20ac'), (b'+AOQ-', 5))
        self.assertEqual(codecs.utf_7_encode(b'\u8f9f'), (b'+3B/qAPA-', 9))

        self.assertEqual(codecs.
