import io
# Test io.RawIOBase (AKA IOBase)
# This would be nice to have in test_io, but that would cause a circular import.
with open(TESTFN, "wb") as f:
    f.write(b"test\n")

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'rb')

    def tearDown(self):
        self.f.close()
        unlink(TESTFN)

    def testReadinto(self):
        b = bytearray(b"xxxxxx")
        n = self.f.readinto(b)
        self.assertEqual(b[:n], b"test\n")
        self.assertEqual(b[n:], b"xxxxxx"[n:])

    def testReadintoArray(self):
        b = array.array("b", b"xxxxxx")
        n = self.f.readinto(b)
        self.assertEqual(b.tobytes()[:n], b"test\n")

