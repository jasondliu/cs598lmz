import io
# Test io.RawIOBase with a file

import _io

class RawIOBaseFileTest(BaseTestCheckIO):
    def test_read(self):
        self.assertEqual(self.io.read(0), b"")
        self.assertEqual(self.io.read(1), b"1")
        self.assertEqual(self.io.read(2), b"23")
        self.assertEqual(self.io.read(5), b"456\n")
        self.assertEqual(self.io.read(1), b"")
        self.assertEqual(self.io.read(0), b"")
        self.assertEqual(self.io.read(), b"")
        self.assertEqual(self.io.read(1), b"")

    def test_read1(self):
        self.assertEqual(self.io.read1(1), b"1")
        self.assertEqual(self.io.read1(2), b"23")
        self.assertEqual(self.io.read1(5),
