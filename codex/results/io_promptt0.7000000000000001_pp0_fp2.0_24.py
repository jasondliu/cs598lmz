import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(BaseTestCase):

    def setUp(self):
        self.rawio = io.RawIOBase()
        self.f = io.BytesIO()

    def tearDown(self):
        self.f.close()
        self.rawio.close()

    def test_readinto(self):
        self.f.write(b"hello")
        n = self.f.tell()
        self.f.seek(0)
        b = bytearray(3)
        self.assertEqual(self.f.readinto(b), 3)
        self.assertEqual(bytes(b), b"hel")
        self.assertEqual(self.f.tell(), n)
        self.assertEqual(self.f.readinto(b), 2)
        self.assertEqual(bytes(b), b"lo")
        self.assertEqual(self.f.readinto(b), 0)
        self.assertEqual(bytes(b), b"lo")

    def test_error
