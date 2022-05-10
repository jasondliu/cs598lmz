import io
# Test io.RawIOBase
class test_RawIOBase:

    def write(self, b):
        io.RawIOBase.write(self, b)
        io.RawIOBase.flush(self)


class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_abstracts(self):
        self.assertRaises(io.UnsupportedOperation, test_RawIOBase().read, 0)
        self.assertRaises(io.UnsupportedOperation, test_RawIOBase().seek, 0, 0)
        self.assertRaises(io.UnsupportedOperation, test_RawIOBase().tell)
        self.assertRaises(io.UnsupportedOperation, test_RawIOBase().truncate, 0)
        self.assertEqual(test_RawIOBase().seekable(), False)
        self.assertEqual(test_RawIOBase().readable(), False)
        self.assertEqual(test_RawIOBase().writable(), False)
        self.assert
