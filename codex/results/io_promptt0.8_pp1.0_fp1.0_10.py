import io
# Test io.RawIOBase.close() when unbuffered.

class RawIOBaseTest(unittest.TestCase):
    def test_close(self):
        # This is a fairly trivial test, but at least it
        # makes sure the method is present.
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.close)
        f = io.BytesIO()
        f.close()
        self.assertRaises(ValueError, f.fileno)
        self.assertRaises(ValueError, f.isatty)
        self.assertRaises(ValueError, f.read)
        self.assertRaises(ValueError, f.readinto, bytearray(1))
        self.assertRaises(ValueError, f.readline)
        self.assertRaises(ValueError, f.readlines)
        self.assertRaises(ValueError, f.write, b'')
        self.assertRaises(ValueError, f.writelines, [])

if __name__ == '__main__':
    unittest
