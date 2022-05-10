import mmap
# Test mmap.mmap(0, 1, "", mmap.ACCESS_READ)

class TestMMap(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        f = open(self.filename, 'w+b')
        try:
            f.write(bytes(bytearray(range(256))))
        finally:
            f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_basic(self):
        f = open(self.filename, 'r+b')
        try:
            m = mmap.mmap(f.fileno(), 256)
            self.assertEqual(len(m), 256)
            self.assertEqual(m[0], 0)
            self.assertEqual(m[0:1], bytes([0]))
            self.assertEqual(m[0:10], bytes(bytearray(range(10))))
            self.assertEqual(m[0:20], bytes(bytearray(range(20
