import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# This should not crash.
view.tobytes()
""")

    def test_readinto_empty_buffer(self):
        # Issue #11108: segfault when calling readinto on an empty buffer
        self.assertRaises(TypeError, f.readinto, bytearray())
        self.assertRaises(TypeError, f.readinto, memoryview(bytearray()))

    def test_readline(self):
        f = self.open(support.TESTFN, 'w+')
        f.write(b'line1\nline2\nline3\n')
        f.seek(0)
        self.assertEqual(f.readline(), b'line1\n')
        self.assertEqual(f.readline(10), b'line2\n')
        self.assertEqual(f.readline(2), b'li')
        self.assertEqual(f.readline(4), b'ne3\n')
        self.assertEqual(f.readline(), b'')

