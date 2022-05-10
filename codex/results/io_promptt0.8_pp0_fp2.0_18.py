import io
# Test io.RawIOBase.
class ReadlineTest(unittest.TestCase):

    def setUp(self):
        self.data = 'line1\nline2\nline3\n'
        self.f = io.BytesIO(self.data.encode('latin-1'))

    def test_readline(self):
        eq = self.assertEqual
        eq(self.f.readline(), b'line1\n')
        eq(self.f.readline(10), b'line2\n')
        eq(self.f.readline(2), b'li')
        eq(self.f.readline(4), b'ne3\n')
        eq(self.f.readline(), b'')

    def test_readline_non_default_size(self):
        line = self.f.readline(1)
        self.assertEqual(line, b'l')
        if sys.maxsize > 2 ** 32:
            match = 'cannot fit ' + repr(sys.maxsize + 1) + ' into an int'

