import io
# Test io.RawIOBase

# io.RawIOBase.readinto()

class TestBasic:
    def test_newlines(self):
        for nl in ['', '\n', '\r', '\r\n']:
            r = io.StringIO('a' + nl + 'b')
            n = r.readline()
            self.assertEqual(n, 'a' + nl)
            n = r.readline()
            self.assertEqual(n, 'b')
            self.assertEqual(r.readline(), '')
            self.assertRaises(TypeError, r.readline, 5)

    def test_readline(self):
        r = io.StringIO(u"Not a newline")
        self.assertRaises(TypeError, r.readline, 0.0)

    def test_truncate(self):
        r = io.StringIO('abc')
        self.assertRaises(IOError, r.truncate, -1)
        r.seek(0, 2)
        r.write('def
