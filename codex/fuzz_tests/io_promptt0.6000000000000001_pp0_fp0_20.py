import io
# Test io.RawIOBase
class RawIOBase_Test(unittest.TestCase):

    def test_readinto(self):
        o = io.RawIOBase()
        self.assertEqual(o.readinto(bytearray(10)), 0)
        self.assertEqual(o.readinto(bytearray(10)), 0)

    def test_readall(self):
        o = io.RawIOBase()
        self.assertEqual(o.readall(), b'')
        self.assertEqual(o.readall(), b'')

class RawIOBase_Readinto_Test(unittest.TestCase):

    def test_readinto(self):
        o = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, o.readinto, bytearray(10))

class RawIOBase_Readinto_Read_Test(unittest.TestCase):

    def test_readinto(self):
        o = io.RawIOBase()
        o.read = lambda n: b'x' * (n - 1
