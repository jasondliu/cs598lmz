import io
# Test io.RawIOBase subclasses.

import _pyio as pyio

class RawInputFileTest(unittest.TestCase):
    def s_test(self, s):
        buf = io.BytesIO()
        b = buf.write(s)

        f = pyio.open(buf, 'rb', closefd=False)
        self.assertEqual(f.read(), s)

    def test_working_readline(self):
        self.s_test(b"1234567-\n")

    def test_weird_reads(self):
        self.s_test(b"1234\r-\n")
        self.s_test(b"1234\r-\r\n")
        self.s_test(b"1234-\r\n")
        self.s_test(b"1234\r\n-\r\n")

    def test_seek_and_tell(self):
        self.s_test(b"123456")
        buf = io.BytesIO(b"123456")

        f = pyio
