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

class StringIOTest(unittest.TestCase):
    def test_write(self):
        s = io.StringIO()
        s.write("abc")
        self.assertEqual(s.getvalue(), "abc")
        s.close()
        self.assertRaises(ValueError, s.write, "abc")

    def test_writelines(self):
        s = io.StringIO()
        s.writelines(("ab", "cd", "ef"))
        self.assertEqual(s.getvalue(), "abcdef")
        s.close()
        self.assertRaises(ValueError, s.writelines, [])

    def test_read(self):
        s = io.StringIO("abc")
        self.assertEqual(s.read(4), "abc")
        self.assertEqual(s.read(1), "")
        s.close()
        self.assertRaises(ValueError, s.read)

    def test_readline(self):
        s = io.StringIO("ab\nc\nd
